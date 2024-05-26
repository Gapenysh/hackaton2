from project import app
from flask import request, jsonify
from project.model_database import Database

@app.route("/construcktor", methods=["POST", "GET"])
def show_resumes():
    if request.method == "POST":
        result = Database.get_all_resumes()
        return jsonify(result)


