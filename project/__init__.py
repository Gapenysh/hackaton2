from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

DB_NAME = "resumes.db"
CORS(app)

from . import constructor