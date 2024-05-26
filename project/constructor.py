from project import app
from flask import request, jsonify
from project.model_database import Database


@app.route("/construcktor", methods=["POST", "GET"])
def show_resumes():
    if request.method == "GET":
        result = Database.get_all_resumes()
        if result is None:
            return "Error: Could not access the database", 500

        return jsonify(result)
    else:
        return jsonify([])


