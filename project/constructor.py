from project import app
from flask import request, jsonify
from project.model_database import Database

@app.route("/construcktor", methods=["POST", "GET"])
def show_rezumes():
    if request.method == "POST":


