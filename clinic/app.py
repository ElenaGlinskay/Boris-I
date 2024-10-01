from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para manejar sesiones

# Simulamos una base de datos de usuarios con un diccionario
users_db = {}

def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Debes iniciar sesión para acceder a esta página.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Inicializamos las rutas
def init_routes(app, users_db, login_required):
    # Rutas públicas
    @app.route('/')
    def home():
        return render_template('layout.html', page='pagesLanding/home.html')

    # ... (el resto de las rutas se adaptan para usar users_db) ...

# Inicializamos las rutas
init_routes(app, users_db, login_required)

if __name__ == '__main__':
    app.run(debug=True)
