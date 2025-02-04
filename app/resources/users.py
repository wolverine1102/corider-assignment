from flask import Blueprint
from flask_restful import Api, Resource

users_bp = Blueprint("users", __name__)
api = Api(users_bp)

class UserResource(Resource):
    def get(self, id=None):
        pass

    def post(self):
        pass

    def put(self, id):
        pass
    
    def delete(self, id):
        pass

api.add_resource(UserResource, "/", "/<string:id>")