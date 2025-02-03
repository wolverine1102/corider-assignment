from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

def admin_setup(mongo: PyMongo, bcrypt: Bcrypt):
    users_collection = mongo.db.Users
    admin = users_collection.find_one({"username": "admin"})

    if admin is None:
        hashed_password = bcrypt.generate_password_hash("admin_password").decode("utf-8")
        users_collection.insert_one({
            "username": "admin",
            "password": hashed_password,
            "role": "admin"
        })
        print("Admin created successfully...")
    else:
        print("Admin already exists. No changes made...")