from flask import Flask
from config import Config
from .extensions import api, mongo, bcrypt, ma, jwt
from .services.admin_setup import admin_setup
from .resources.auth import auth_bp
from .resources.users import users_bp

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

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(users_bp, url_prefix="/api/users")

    return app