from flask_restful import Api
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

api = Api()
mongo = PyMongo()
bcrypt = Bcrypt()