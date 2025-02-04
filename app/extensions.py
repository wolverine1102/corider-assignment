from flask_restful import Api
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

api = Api()
mongo = PyMongo()
bcrypt = Bcrypt()
ma = Marshmallow()
jwt = JWTManager()

@jwt.user_identity_loader
def user_identity_lookup(user):
    return {
        "id": user["id"],
        "role": user["role"]
    }