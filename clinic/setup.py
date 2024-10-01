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
        "templates/pagesCitas"
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

# Simulamos una base de datos de usuarios y citas
users_db = {}
specialties_db = {}  # Especialidades
doctors_db = {}  # Médicos
appointments_db = {}  # Citas

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
init_routes(app, users_db, specialties_db, doctors_db, appointments_db, login_required)

if __name__ == '__main__':
    app.run(debug=True)
"""
    with open("app.py", "w") as f:
        f.write(app_code)

# Crea el archivo utils/routes.py
def create_routes_file():
    routes_code = """
from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

def init_routes(app, users_db, specialties_db, doctors_db, appointments_db, login_required):

    # Rutas públicas
    @app.route('/')
    def home():
        return render_template('layout.html', page='pagesLanding/home.html')

    @app.route('/especialidades')
    def specialties():
        return render_template('layout.html', page='pagesLanding/specialties.html', specialties=specialties_db)

    @app.route('/medicos')
    def doctors():
        return render_template('layout.html', page='pagesLanding/doctors.html', doctors=doctors_db)

    @app.route('/horarios')
    def schedules():
        return render_template('layout.html', page='pagesLanding/schedules.html', doctors=doctors_db)

    # Registro y Login
    @app.route('/registro', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            if username in users_db:
                flash('El nombre de usuario ya existe.')
                return redirect(url_for('register'))
            
            hashed_password = generate_password_hash(password, method='sha256')
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
                return redirect(url_for('dashboard'))
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

    @app.route('/citas')
    @login_required
    def appointments():
        return render_template('layout.html', page='pagesCitas/citas.html', appointments=appointments_db.get(session['username'], []))

    @app.route('/crear_cita', methods=['GET', 'POST'])
    @login_required
    def create_appointment():
        if request.method == 'POST':
            specialty = request.form['specialty']
            doctor = request.form['doctor']
            date = request.form['date']
            time = request.form['time']
            
            if specialty not in specialties_db or doctor not in doctors_db:
                flash('Especialidad o médico no válido.')
                return redirect(url_for('create_appointment'))
            
            appointment = {
                'specialty': specialty,
                'doctor': doctor,
                'date': date,
                'time': time
            }
            
            if session['username'] not in appointments_db:
                appointments_db[session['username']] = []
            
            appointments_db[session['username']].append(appointment)
            flash('Cita creada con éxito.')
            return redirect(url_for('appointments'))
        
        return render_template('layout.html', page='pagesCitas/create_appointment.html', specialties=specialties_db, doctors=doctors_db)
"""
    with open("utils/routes.py", "w") as f:
        f.write(routes_code)

# Crea el archivo controllers/backend/specialty_controller.py
def create_specialty_controller():
    specialty_code = """
def add_specialty(specialties_db, name):
    if name in specialties_db:
        return False  # Especialidad ya existe
    specialties_db[name] = {'name': name}
    return True  # Especialidad agregada con éxito
"""
    os.makedirs("controllers/backend", exist_ok=True)
    with open("controllers/backend/specialty_controller.py", "w") as f:
        f.write(specialty_code)

# Crea el archivo controllers/backend/doctor_controller.py
def create_doctor_controller():
    doctor_code = """
def add_doctor(doctors_db, name, specialty, schedule):
    if name in doctors_db:
        return False  # Médico ya existe
    doctors_db[name] = {'name': name, 'specialty': specialty, 'schedule': schedule}
    return True  # Médico agregado con éxito
"""
    with open("controllers/backend/doctor_controller.py", "w") as f:
        f.write(doctor_code)

# Crea las plantillas para las páginas de citas y especialidades
def create_citas_pages():
    citas_pages = {
        "citas.html": "<h1>Tus Citas</h1><ul>{% for cita in appointments %}<li>{{ cita['specialty'] }} con {{ cita['doctor'] }} el {{ cita['date'] }} a las {{ cita['time'] }}</li>{% endfor %}</ul>",
        "create_appointment.html": """
<form method="POST">
    <label for="specialty">Especialidad:</label>
    <select name="specialty" required>
        {% for name, specialty in specialties.items() %}
        <option value="{{ name }}">{{ name }}</option>
        {% endfor %}
    </select>
    <label for="doctor">Médico:</label>
    <select name="doctor" required>
        {% for name, doctor in doctors.items() %}
        <option value="{{ name }}">{{ name }} - {{ doctor['specialty'] }}</option>
        {% endfor %}
    </select>
    <label for="date">Fecha:</label>
    <input type="date" name="date" required>
    <label for="time">Hora:</label>
    <input type="time" name="time" required>
    <button type="submit">Reservar Cita</button>
</form>
"""
    }
    
    for filename, content in citas_pages.items():
        with open(f"templates/pagesCitas/{filename}", "w") as f:
            f.write(content)

if __name__ == "__main__":
    create_structure()
    create_app_file()
    create_routes_file()
    create_specialty_controller()
    create_doctor_controller()
    create_citas_pages()
    print("Estructura de proyecto creada con éxito.")
