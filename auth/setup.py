
# # setup.py
# import os

# # Crea la estructura de directorios
# def create_structure():
#     directories = [
#         "utils",
#         "routes/backend",
#         "routes/frontend",
#         "controllers/backend",
#         "controllers/frontend",
#         "templates/pagesLanding",
#         "templates/pagesDashboard",
#     ]
    
#     for directory in directories:
#         os.makedirs(directory, exist_ok=True)

# # Crea el archivo app.py
# def create_app_file():
#     app_code = """
# from flask import Flask, render_template, request, redirect, url_for, session, flash
# from utils.routes import init_routes

# app = Flask(__name__)
# app.secret_key = 'supersecretkey'  # Necesario para manejar sesiones

# # Simulamos una base de datos de usuarios con un diccionario
# users_db = {}

# def login_required(f):
#     from functools import wraps
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if 'username' not in session:
#             flash('Debes iniciar sesión para acceder a esta página.')
#             return redirect(url_for('login'))
#         return f(*args, **kwargs)
#     return decorated_function

# # Inicializamos las rutas
# init_routes(app, users_db, login_required)

# if __name__ == '__main__':
#     app.run(debug=True)
# """
#     with open("app.py", "w") as f:
#         f.write(app_code)

# # Crea el archivo utils/routes.py
# def create_routes_file():
#     routes_code = """
# from flask import render_template, request, redirect, url_for, flash
# from werkzeug.security import generate_password_hash, check_password_hash  # Asegúrate de que esto esté importado

# def init_routes(app, users_db, login_required):
    
#     # Rutas públicas
#     @app.route('/')
#     def home():
#         return render_template('layout.html', page='pagesLanding/home.html')

#     @app.route('/sobre_nosotros')
#     def about():
#         return render_template('layout.html', page='pagesLanding/about.html')

#     @app.route('/servicios')
#     def services():
#         return render_template('layout.html', page='pagesLanding/services.html')

#     @app.route('/registro', methods=['GET', 'POST'])
#     def register():
#         if request.method == 'POST':
#             username = request.form['username']
#             password = request.form['password']
            
#             if username in users_db:
#                 flash('El nombre de usuario ya existe.')
#                 return redirect(url_for('register'))
            
#             hashed_password = generate_password_hash(password, method='sha256')  # Esta línea debe funcionar ahora
#             users_db[username] = hashed_password
#             flash('Registro exitoso. Ahora puedes iniciar sesión.')
#             return redirect(url_for('login'))
#         return render_template('layout.html', page='pagesLanding/register.html')

#     @app.route('/login', methods=['GET', 'POST'])
#     def login():
#         if request.method == 'POST':
#             username = request.form['username']
#             password = request.form['password']
            
#             if username in users_db and check_password_hash(users_db[username], password):
#                 session['username'] = username
#                 flash('Inicio de sesión exitoso.')
#                 return redirect(url_for('dashboard'))  # Redirige a dashboard
#             flash('Nombre de usuario o contraseña incorrectos.')
#         return render_template('layout.html', page='pagesLanding/login.html')

#     @app.route('/logout')
#     def logout():
#         session.pop('username', None)
#         flash('Has cerrado sesión.')
#         return redirect(url_for('home'))

#     # Rutas privadas (requieren autenticación)
#     @app.route('/dashboard')
#     @login_required
#     def dashboard():
#         return render_template('layout.html', page='pagesDashboard/users.html')

#     @app.route('/roles')
#     @login_required
#     def roles():
#         return render_template('layout.html', page='pagesDashboard/roles.html')
# """
#     with open("utils/routes.py", "w") as f:
#         f.write(routes_code)

# # Crea el archivo controllers/backend/auth_controller.py
# def create_auth_controller():
#     auth_code = """
# from werkzeug.security import generate_password_hash, check_password_hash

# def register_user(users_db, username, password):
#     if username in users_db:
#         return False  # Usuario ya existe
#     users_db[username] = generate_password_hash(password, method='sha256')
#     return True  # Registro exitoso

# def verify_user(users_db, username, password):
#     if username in users_db and check_password_hash(users_db[username], password):
#         return True  # Credenciales correctas
#     return False  # Credenciales incorrectas
# """
#     os.makedirs("controllers/backend", exist_ok=True)
#     with open("controllers/backend/auth_controller.py", "w") as f:
#         f.write(auth_code)

# # Crea el archivo templates/layout.html
# def create_layout_file():
#     layout_code = """
# <!DOCTYPE html>
# <html lang="es">
# <head>
#     <meta charset="UTF-8">
#     <title>Mi Aplicación Flask</title>
# </head>
# <body>
#     <nav>
#         <ul>
#             <li><a href="/">Inicio</a></li>
#             <li><a href="/sobre_nosotros">Sobre Nosotros</a></li>
#             <li><a href="/servicios">Servicios</a></li>
#             {% if session.username %}
#                 <li><a href="/logout">Cerrar Sesión</a></li>
#             {% else %}
#                 <li><a href="/login">Iniciar Sesión</a></li>
#                 <li><a href="/registro">Registro</a></li>
#             {% endif %}
#         </ul>
#     </nav>

#     {% with messages = get_flashed_messages() %}
#       {% if messages %}
#         <ul>
#         {% for message in messages %}
#           <li>{{ message }}</li>
#         {% endfor %}
#         </ul>
#       {% endif %}
#     {% endwith %}

#     <div>
#         {% include page %}
#     </div>
# </body>
# </html>
# """
#     with open("templates/layout.html", "w") as f:
#         f.write(layout_code)

# # Crea archivos de las páginas de Landing
# def create_landing_pages():
#     landing_pages = {
#         "home.html": "<h1>Bienvenido a nuestra página de inicio</h1>",
#         "about.html": "<h1>Sobre Nosotros</h1><p>Información sobre nuestra empresa.</p>",
#         "services.html": "<h1>Servicios</h1><p>Lista de servicios ofrecidos.</p>",
#         "register.html": """
# <form method="POST">
#     <input type="text" name="username" placeholder="Nombre de usuario" required>
#     <input type="password" name="password" placeholder="Contraseña" required>
#     <button type="submit">Registrarse</button>
# </form>
# """,
#         "login.html": """
# <form method="POST">
#     <input type="text" name="username" placeholder="Nombre de usuario" required>
#     <input type="password" name="password" placeholder="Contraseña" required>
#     <button type="submit">Iniciar Sesión</button>
# </form>
# """,
#     }
    
#     for filename, content in landing_pages.items():
#         with open(f"templates/pagesLanding/{filename}", "w") as f:
#             f.write(content)

# # Crea archivos de las páginas de Dashboard
# def create_dashboard_pages():
#     dashboard_pages = {
#         "users.html": "<h1>Usuarios</h1><p>Lista de usuarios registrados.</p>",
#         "roles.html": "<h1>Roles</h1><p>Lista de roles disponibles.</p>",
#     }
    
#     for filename, content in dashboard_pages.items():
#         with open(f"templates/pagesDashboard/{filename}", "w") as f:
#             f.write(content)

# if __name__ == "__main__":
#     create_structure()
#     create_app_file()
#     create_routes_file()
#     create_auth_controller()
#     create_layout_file()
#     create_landing_pages()
#     create_dashboard_pages()
#     print("Estructura de proyecto creada con éxito.")


import os

# Estructura de archivos
directories = [
    "medical_appointments",
    "medical_appointments/templates",
    "medical_appointments/static"
]

files = {
    "medical_appointments/app.py": """from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_session import Session
from datetime import datetime
from forms import RegistrationForm, LoginForm
from models import User, Medico, Paciente, Cita, Especialidad

app = Flask(__name__)

# Configuración de MongoDB
app.config['MONGODB_SETTINGS'] = {
    'db': 'medical_appointments_db',
    'host': 'localhost',
    'port': 27017,
}
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'

db = MongoEngine(app)
bcrypt = Bcrypt(app)
Session(app)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_password, role=form.role.data)
        user.save()
        flash('Usuario registrado correctamente', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['user_id'] = str(user.id)
            session['role'] = user.role
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciales inválidas', 'danger')
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', role=session['role'])

@app.route('/citas', methods=['GET', 'POST'])
def manage_citas():
    if request.method == 'POST':
        data = request.form
        cita = Cita(
            paciente_id=data['paciente_id'],
            medico_id=data['medico_id'],
            especialidad_id=data['especialidad_id'],
            fecha=datetime.fromisoformat(data['fecha']),
            estado="Pendiente"
        )
        cita.save()
        flash('Cita creada', 'success')
        return redirect(url_for('manage_citas'))
    citas = Cita.objects()
    return render_template('citas.html', citas=citas)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('role', None)
    flash('Has cerrado sesión', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
""",
    "medical_appointments/models.py": """from flask_mongoengine import MongoEngine

db = MongoEngine()

class User(db.Document):
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    role = db.StringField(required=True)  # Super Admin, Admin, Medico, Paciente

class Medico(User):
    nombre = db.StringField(required=True)
    especialidades = db.ListField(db.StringField())

class Paciente(User):
    nombre = db.StringField(required=True)
    telefono = db.StringField()
    citas = db.ListField(db.ReferenceField('Cita'))

class Especialidad(db.Document):
    nombre = db.StringField(required=True)
    descripcion = db.StringField()

class Cita(db.Document):
    paciente_id = db.ReferenceField(Paciente)
    medico_id = db.ReferenceField(Medico)
    especialidad_id = db.ReferenceField(Especialidad)
    fecha = db.DateTimeField()
    estado = db.StringField(choices=["Pendiente", "Confirmada", "Cancelada"])
""",
    "medical_appointments/forms.py": """from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    role = SelectField('Role', choices=[('Paciente', 'Paciente'), ('Medico', 'Médico')], validators=[DataRequired()])
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')
""",
    "medical_appointments/templates/base.html": """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    <title>Gestión de Citas Médicas</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('home') }}">Inicio</a></li>
            <li><a href="{{ url_for('register') }}">Registro</a></li>
            <li><a href="{{ url_for('login') }}">Iniciar Sesión</a></li>
            {% if session['user_id'] %}
                <li><a href="{{ url_for('dashboard') }}">Dashboard</a></li>
                <li><a href="{{ url_for('logout') }}">Cerrar Sesión</a></li>
            {% endif %}
        </ul>
    </nav>
    <div class="container">
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
                </ul>
            {% endif %}
        {% endwith %}
        {% block content %}{% endblock %}
    </div>
</body>
</html>
""",
    "medical_appointments/templates/login.html": """{% extends 'base.html' %}

{% block content %}
    <h2>Iniciar Sesión</h2>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.email.label }} {{ form.email() }}
        </div>
        <div>
            {{ form.password.label }} {{ form.password() }}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
{% endblock %}
""",
    "medical_appointments/templates/register.html": """{% extends 'base.html' %}

{% block content %}
    <h2>Registro</h2>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.email.label }} {{ form.email() }}
        </div>
        <div>
            {{ form.password.label }} {{ form.password() }}
        </div>
        <div>
            {{ form.role.label }} {{ form.role() }}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
{% endblock %}
""",
    "medical_appointments/templates/dashboard.html": """{% extends 'base.html' %}

{% block content %}
    <h2>Dashboard</h2>
    <p>Bienvenido, {{ session['role'] }}!</p>
{% endblock %}
""",
    "medical_appointments/templates/citas.html": """{% extends 'base.html' %}

{% block content %}
    <h2>Gestionar Citas</h2>
    <form method="POST">
        <div>
            <label for="paciente_id">ID del Paciente:</label>
            <input type="text" id="paciente_id" name="paciente_id" required>
        </div>
        <div>
            <label for="medico_id">ID del Médico:</label>
            <input type="text" id="medico_id" name="medico_id" required>
        </div>
        <div>
            <label for="especialidad_id">ID de la Especialidad:</label>
            <input type="text" id="especialidad_id" name="especialidad_id" required>
        </div>
        <div>
            <label for="fecha">Fecha:</label>
            <input type="datetime-local" id="fecha" name="fecha" required>
        </div>
        <div>
            <button type="submit">Crear Cita</button>
        </div>
    </form>
    
    <h3>Citas Existentes</h3>
    <ul>
        {% for cita in citas %}
            <li>Cita de {{ cita.paciente_id.nombre }} con {{ cita.medico_id.nombre }} el {{ cita.fecha }} - Estado: {{ cita.estado }}</li>
        {% endfor %}
    </ul>
{% endblock %}
""",
    "medical_appointments/static/styles.css": """body {
    font-family: Arial, sans-serif;
}

nav {
    background-color: #333;
    padding: 10px;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin-right: 20px;
}

nav ul li a {
    color: white;
    text-decoration: none;
}

.container {
    padding: 20px;
}

h2, h3 {
    color: #333;
}
"""
}

# Crear directorios y archivos
for directory in directories:
    os.makedirs(directory, exist_ok=True)

for file_path, file_content in files.items():
    with open(file_path, 'w') as f:
        f.write(file_content)

print("Estructura de proyecto creada con éxito.")
print("Ejecuta 'pip install -r requirements.txt' para instalar las dependencias.")
