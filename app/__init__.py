from flask import Flask
from config import config
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(app.config.from_object(config['development']))

db = SQLAlchemy(app)

from app import views, models

if __name__ == "__main__":
    db.create_all()
    db.session.commit()
