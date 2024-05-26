import sqlite3
from project import app, DB_NAME_TEAMS
from project.model_database import Database
from flask import request, jsonify

def get_db_connection():
    conn = sqlite3.connect(DB_NAME_TEAMS)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/construcktor/teams', methods=['POST'])
def create_team():
    data = request.get_json()
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO teams (name, size, roles, members, status) VALUES (?, ?, ?, ?, ?)',
                     (data['name'], data['size'], ','.join(data['roles']), ','.join(data['members']), 'pending'))
        conn.commit()
        conn.close()
        print("Команда создана")
        return jsonify({'message': 'Team created successfully'})
    except sqlite3.Error as e:
        print("Ошибка получения доступа к БД" + str(e))
        return None
    finally:
        conn.close()

@app.route('/construcktor/teams', methods=['GET'])
def get_team():
    conn = get_db_connection()
    teams = conn.execute('SELECT * FROM teams').fetchall()
    result = []
    for team in teams:
        members = team['members'].split(',') if team['members'] else []
        result.append({
            'id': team['id'],
            'name': team['name'],
            'size': team['size'],
            'roles': team['roles'].split(','),
            'members': members,
            'status': team['status']
        })
    conn.close()
    return jsonify(result)


@app.route('/api/teams/<int:team_id>', methods=['PUT'])
def update_team(team_id):
    data = request.get_json()
    conn = get_db_connection()

    # Обновить статус команды, если необходимо
    team = conn.execute('SELECT members, status FROM teams WHERE id = ?', (team_id,)).fetchone()
    members = team['members'].split(',') if team['members'] else []
    ready_members = [member for member in members if member.endswith('(ready)')]
    if data['status'] == 'ready' and len(ready_members) * 2 < len(members):
        conn.close()
        return jsonify({'message': 'Not enough members are ready'}), 400
    elif data['status'] == 'pending' and len(ready_members) * 2 >= len(members):
        conn.close()
        return jsonify({'message': 'Cannot change status to pending'}), 400

    conn.execute('UPDATE teams SET status = ? WHERE id = ?', (data['status'], team_id))
    conn.commit()

    conn.close()
    return jsonify({'message': 'Team updated successfully'})
