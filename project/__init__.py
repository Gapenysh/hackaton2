from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

DB_NAME = "resumes.db"
DB_NAME_TEAMS = "teams.db"

CORS(app)

from . import constructor, create_resume, create_team