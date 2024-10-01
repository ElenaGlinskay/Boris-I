# config.py
class Config:
    SECRET_KEY = 'tu_clave_secreta'  # Cambia esto por una clave secreta segura
    MONGO_URI = 'mongodb://localhost:27017/tu_base_de_datos'  # URI de tu base de datos MongoDB

config = Config()
