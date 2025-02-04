import os
from dotenv import load_dotenv

load_dotenv()

MONGO_USERNAME = os.getenv('USERNAME')
MONGO_PASSWORD = os.getenv('PASSWORD')
MONGO_HOSTNAME = os.getenv('HOSTNAME')
MONGO_PORT = os.getenv('PORT')
MONGO_DB = os.getenv('DB')

class Config:
    MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOSTNAME}:{MONGO_PORT}/{MONGO_DB}?authSource=admin"

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES  = 3600