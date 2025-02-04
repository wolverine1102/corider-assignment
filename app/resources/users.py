from flask import Blueprint, request
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from ..extensions import mongo, bcrypt
from ..schemas.users import user_schema, users_schema
from ..utils.id_generator import generate_random_id
from ..errors.exceptions import BusinessValidationError

users_bp = Blueprint("users", __name__)
api = Api(users_bp)

class UserResource(Resource):
    @jwt_required()
    def get(self, id=None):
        current_user = mongo.db.users.find_one({"id": get_jwt_identity()})
        if id:
            if current_user["id"] == id or current_user["role"] == "admin":
                user = mongo.db.users.find_one({"id": id})
                if user:
                    response = user_schema.dump(user)
                    return response, 200
                else:
                    raise BusinessValidationError(
                        status_code=404,
                        error_message="User not found"
                    )
                
            else:
                raise BusinessValidationError(
                    status_code=401,
                    error_message="Unauthorized: Authentication required"
                )

        else:
            if current_user["role"] == "admin":
                users = mongo.db.users.find({})
                response = users_schema.dump(users)
                return response, 200
            else:
                raise BusinessValidationError(
                    status_code=403,
                    error_message="Forbidden: You do not have permission to access this resource"
                )
    
    @jwt_required()
    def post(self):
        current_user = mongo.db.users.find_one({"id": get_jwt_identity()})
        if current_user["role"] == "admin":
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
                return response, 200
            
            else:
                raise BusinessValidationError(
                    status_code=400,
                    error_message="User with this email already exists"
                )

        else:
            raise BusinessValidationError(
                    status_code=403,
                    error_message="Forbidden: You do not have permission to access this resource"
                )
    
    @jwt_required()
    def put(self, id):
        current_user = mongo.db.users.find_one({"id": get_jwt_identity()})
        if current_user["id"] == id or current_user["role"] == "admin":
            try:
                data = user_schema.load(request.get_json(), partial=True)
            except ValidationError as err:
                return err.messages, 400
            
            if "role" in data:
                    if current_user.get("role") != "admin":
                        raise BusinessValidationError(
                            status_code=403,
                            error_message="You do not have permission to update the role"
                        )
            
            updated_data = {key: value for key, value in data.items()}
            update = mongo.db.users.update_one({"id": id}, {"$set": updated_data})

            if update.matched_count > 0:
                updated_user = mongo.db.users.find_one({"id": id})
                response = user_schema.dump(updated_user)
                return response, 200
                
            else:
                raise BusinessValidationError(
                        status_code=404,
                        error_message="User not found"
                    )
        else:
            raise BusinessValidationError(
                status_code=401,
                error_message="Unauthorized: Authentication required"
            )

    
    @jwt_required()
    def delete(self, id):
        current_user = mongo.db.users.find_one({"id": get_jwt_identity()})
        if current_user["id"] == id or current_user["role"] == "admin":
                deleted_user = mongo.db.users.delete_one({"id": id})
                if deleted_user.deleted_count:
                    return {
                         "message": "User deleted successfully"
                    }, 200
                
                else:
                    raise BusinessValidationError(
                        status_code=404,
                        error_message="User not found or already deleted"
                    )
        else:
            raise BusinessValidationError(
                status_code=401,
                error_message="Unauthorized: Authentication required"
            )


api.add_resource(UserResource, "/", "/<string:id>")