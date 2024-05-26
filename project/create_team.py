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
    name = request.json.get("teamName", None)
    size = request.json.get("teamSize", None)
    roles = request.json.get("selectedRoles", None)
    if (name, size, roles) is not None:
        res = Database.add_team(name, size, roles)
        if res:
            print("Команда добавлена в БД")
            return jsonify({"message": "Command added"})
        else:
            print("Ошибка создания команды")
            return jsonify({"error": "Command not added"})
    else:
        print("Переменная яв-ся None")
        return jsonify({"error": "parametr is None"})

@app.route("/construcktor/teams", methods=["GET"])
def show_teams():
    result = Database.get_all_teams()
    if result is None:
        return "Error: Could not access the database", 500
    return jsonify(result)
