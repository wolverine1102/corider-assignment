from flask import Flask
from config import Config
from .extensions import api, mongo, bcrypt, ma, jwt
from .services.admin_setup import admin_setup

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    api.init_app(app)
    mongo.init_app(app)
    bcrypt.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        admin_setup(mongo, bcrypt)

    return app