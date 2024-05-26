import sqlite3

from project import app
from project.model_database import Database
from flask import request, jsonify
@app.route('/construcktor/teams', methods=['POST'])
def create_team():
    data = request.get_json()
    conn = Database.conn_row()
    try:
        conn.execute('INSERT INTO teams (name, size, roles, members, status) VALUES (?, ?, ?, ?, ?)',
                     (data['name'], data['size'], ','.join(data['roles']), ','.join(data['members']), 'pending'))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Team created successfully'})
    except sqlite3.Error as e:
        print("Ошибка получения доступа к БД" + str(e))
        return None
    finally:
        conn.close()

@app.route('/construcktor/teams', methods=['GET'])
def get_team():
    conn = Database.conn_row()
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