# config.py
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables de entorno del archivo .env

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')  # Clave secreta desde .env
    MONGO_URI = os.getenv('MONGO_URI')  # URI de la base de datos desde .env

config = Config()
