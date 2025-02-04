from flask import Blueprint, request
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token
from marshmallow import ValidationError
from ..extensions import mongo, bcrypt
from ..schemas.users import user_schema
from ..utils.id_generator import generate_random_id
from ..errors.exceptions import BusinessValidationError


auth_bp = Blueprint("auth", __name__)
api = Api(auth_bp)

class LoginResource(Resource):
    def post(self):
        try:
            data = user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        user = mongo.db.users.find_one({"email": data["email"]})
        if not user or not bcrypt.check_password_hash(user["password"], data["password"]):
            raise BusinessValidationError(
                status_code=401, 
                error_message="Invalid email or password"
            )
        
        else:
            response = user_schema.dump(user)
            response["token"] = create_access_token(identity=user["id"])
            return response, 200
                 

class RegisterResource(Resource):
    def post(self):
        try:
            data = user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400
        
        existing_user = mongo.db.users.find_one({"email": data["email"]})
        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
            data["id"] = generate_random_id()
            data["password"] = hashed_password

            inserted_user = mongo.db.users.insert_one(data)
            new_user = mongo.db.users.find_one({"_id": inserted_user.inserted_id})

            response = user_schema.dump(new_user)
            response["token"] = create_access_token(identity=new_user["id"])
            return response, 200

        else:
            raise BusinessValidationError(
                status_code=400,
                error_message="User with this email already exists"
            )


api.add_resource(LoginResource, "/login")
api.add_resource(RegisterResource, "/register")