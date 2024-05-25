from flask import Flask, request
from project import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
import uuid
import os

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



