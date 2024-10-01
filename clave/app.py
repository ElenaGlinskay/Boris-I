from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo  # Asegúrate de que esto esté importado correctamente
from utils.routes import init_routes

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para manejar sesiones

# Configuración de MongoDB
app.config['MONGO_URI'] = 'mongodb+srv://police:police@cluster0.j7bgf.mongodb.net/clinicaGranPoosi?retryWrites=true&w=majority'  # Cambia esto según tu configuración
mongo = PyMongo(app)  # Inicializa la instancia de PyMongo

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
init_routes(app, mongo, login_required)

if __name__ == '__main__':
    app.run(debug=True)
