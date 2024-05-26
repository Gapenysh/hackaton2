from project import app
from flask import request, jsonify
from project.model_database import Database

@app.route("/construcktor/create_resume", methods=["POST", "GET"])
def create_resume():
    if request.method == "POST":
        name = request.json.get("name", None)
        role = request.json.get("role", None)
        skills = request.json.get("skills", None)

        if (name, role, skills) is not None:
            res = Database.add_resume(name, role, skills)
            if res:
                print("Резюме создано")
                return jsonify({"message": "Resume created"})
            else:
                print("Ошибка создания резюме")
                return jsonify({"error": "Resume not created"})



