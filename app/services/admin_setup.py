import os
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

def admin_setup(mongo: PyMongo, bcrypt: Bcrypt):
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

    users_collection = mongo.db.users
    admin = users_collection.find_one({"email": f"{ADMIN_EMAIL}"})

    if admin is None:
        hashed_password = bcrypt.generate_password_hash(f"{ADMIN_PASSWORD}").decode("utf-8")
        users_collection.insert_one({
            "email": f"{ADMIN_EMAIL}",
            "password": hashed_password,
            "role": "admin"
        })
        print("Admin created successfully...")
    else:
        print("Admin already exists. No changes made...")