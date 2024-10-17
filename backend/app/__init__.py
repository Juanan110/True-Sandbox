from flask import Flask
from .database import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cat_cafe_user:password@db:5432/cat_cafe_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from . import routes

        db.create_all()  # Crea las tablas en la base de datos

    return app
