from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from extensions import db

load_dotenv()

app = Flask(__name__)
CORS(app)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

from models import Client, Case
with app.app_context():
    db.create_all()

from routes import api
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)
