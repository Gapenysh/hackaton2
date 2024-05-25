from project import app
from flask import request, jsonify
from project.model_database import Database

@app.route("/add_idea", methods=["POST", "GET"])
def enter_idea():
    if request.method == "POST":
        name = request.json.get("name", None)
        descrip = request.json.get("description", None)
        image = request.json.get("image", None)
        if name and descrip:
            res = Database.add_idea(name, descrip, image)
            if res:
                print("Идея добавлена успешно")
                return jsonify({"message": "Idea added successfully"}), 201
            else:
                print("Ошибка добавлении идеи в БД")
                return jsonify({"message": "Invalid input, please provide name and description"}), 400
        else:
            return jsonify({"message": "Invalid method, this route only accepts POST requests"}), 405


