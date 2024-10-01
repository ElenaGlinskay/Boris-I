# setup.py
import os

# Crea la estructura de directorios
def create_structure():
    directories = [
        "utils",
        "routes/backend",
        "routes/frontend",
        "controllers/backend",
        "controllers/frontend",
        "templates/pagesLanding",
        "templates/pagesDashboard",
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

# Crea el archivo app.py
def create_app_file():
    app_code = """
from flask import Flask, render_template, request, redirect, url_for, session, flash
from utils.routes import init_routes

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
init_routes(app, users_db, login_required)

if __name__ == '__main__':
    app.run(debug=True)
"""
    with open("app.py", "w") as f:
        f.write(app_code)

# Crea el archivo utils/routes.py
def create_routes_file():
    routes_code = """
from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash  # Asegúrate de que esto esté importado

def init_routes(app, users_db, login_required):
    
    # Rutas públicas
    @app.route('/')
    def home():
        return render_template('layout.html', page='pagesLanding/home.html')

    @app.route('/sobre_nosotros')
    def about():
        return render_template('layout.html', page='pagesLanding/about.html')

    @app.route('/servicios')
    def services():
        return render_template('layout.html', page='pagesLanding/services.html')

    @app.route('/registro', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            if username in users_db:
                flash('El nombre de usuario ya existe.')
                return redirect(url_for('register'))
            
            hashed_password = generate_password_hash(password, method='sha256')  # Esta línea debe funcionar ahora
            users_db[username] = hashed_password
            flash('Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect(url_for('login'))
        return render_template('layout.html', page='pagesLanding/register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            if username in users_db and check_password_hash(users_db[username], password):
                session['username'] = username
                flash('Inicio de sesión exitoso.')
                return redirect(url_for('dashboard'))  # Redirige a dashboard
            flash('Nombre de usuario o contraseña incorrectos.')
        return render_template('layout.html', page='pagesLanding/login.html')

    @app.route('/logout')
    def logout():
        session.pop('username', None)
        flash('Has cerrado sesión.')
        return redirect(url_for('home'))

    # Rutas privadas (requieren autenticación)
    @app.route('/dashboard')
    @login_required
    def dashboard():
        return render_template('layout.html', page='pagesDashboard/users.html')

    @app.route('/roles')
    @login_required
    def roles():
        return render_template('layout.html', page='pagesDashboard/roles.html')
"""
    with open("utils/routes.py", "w") as f:
        f.write(routes_code)

# Crea el archivo controllers/backend/auth_controller.py
def create_auth_controller():
    auth_code = """
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
"""
    os.makedirs("controllers/backend", exist_ok=True)
    with open("controllers/backend/auth_controller.py", "w") as f:
        f.write(auth_code)

# Crea el archivo templates/layout.html
def create_layout_file():
    layout_code = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Aplicación Flask</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/sobre_nosotros">Sobre Nosotros</a></li>
            <li><a href="/servicios">Servicios</a></li>
            {% if session.username %}
                <li><a href="/logout">Cerrar Sesión</a></li>
            {% else %}
                <li><a href="/login">Iniciar Sesión</a></li>
                <li><a href="/registro">Registro</a></li>
            {% endif %}
        </ul>
    </nav>

    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <ul>
        {% for message in messages %}
          <li>{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}

    <div>
        {% include page %}
    </div>
</body>
</html>
"""
    with open("templates/layout.html", "w") as f:
        f.write(layout_code)

# Crea archivos de las páginas de Landing
def create_landing_pages():
    landing_pages = {
        "home.html": "<h1>Bienvenido a nuestra página de inicio</h1>",
        "about.html": "<h1>Sobre Nosotros</h1><p>Información sobre nuestra empresa.</p>",
        "services.html": "<h1>Servicios</h1><p>Lista de servicios ofrecidos.</p>",
        "register.html": """
<form method="POST">
    <input type="text" name="username" placeholder="Nombre de usuario" required>
    <input type="password" name="password" placeholder="Contraseña" required>
    <button type="submit">Registrarse</button>
</form>
""",
        "login.html": """
<form method="POST">
    <input type="text" name="username" placeholder="Nombre de usuario" required>
    <input type="password" name="password" placeholder="Contraseña" required>
    <button type="submit">Iniciar Sesión</button>
</form>
""",
    }
    
    for filename, content in landing_pages.items():
        with open(f"templates/pagesLanding/{filename}", "w") as f:
            f.write(content)

# Crea archivos de las páginas de Dashboard
def create_dashboard_pages():
    dashboard_pages = {
        "users.html": "<h1>Usuarios</h1><p>Lista de usuarios registrados.</p>",
        "roles.html": "<h1>Roles</h1><p>Lista de roles disponibles.</p>",
    }
    
    for filename, content in dashboard_pages.items():
        with open(f"templates/pagesDashboard/{filename}", "w") as f:
            f.write(content)

if __name__ == "__main__":
    create_structure()
    create_app_file()
    create_routes_file()
    create_auth_controller()
    create_layout_file()
    create_landing_pages()
    create_dashboard_pages()
    print("Estructura de proyecto creada con éxito.")
