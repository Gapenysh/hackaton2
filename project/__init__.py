from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

DB_NAME = "images_test.db"
UPLOAD_FOLDER = '/path/to/your/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
CORS(app)

from . import add_idea