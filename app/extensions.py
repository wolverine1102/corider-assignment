from flask_restful import Api
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

api = Api()
mongo = PyMongo()
bcrypt = Bcrypt()
ma = Marshmallow()