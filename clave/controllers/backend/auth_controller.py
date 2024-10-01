
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(users_db, username, password):
    if username in users_db:
        return False  # Usuario ya existe
    users_db[username] = generate_password_hash(password, method='sha256')
    return True  # Registro exitoso

def verify_user(users_db, username, password):
    if username in users_db and check_password_hash(users_db[username], password):
        return True  # Credenciales correctas
    return False  # Credenciales incorrectas
