from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para manejar sesiones

# Configuración de MongoDB
app.config['MONGO_URI'] = 'mongodb+srv://fanoro1945:fanoro1945@cluster0.j7bgf.mongodb.net/ThesesIniaf?retryWrites=true&w=majority'
mongo = PyMongo(app)

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
def init_routes(app):
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

  
    @app.route('/especialidades')
    def specialties():
        specialties_db = mongo.db.specialties.find()
        return render_template('layout.html', page='pagesLanding/specialties.html', specialties=specialties_db)


    # Registro y Login
    @app.route('/registro', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            if mongo.db.users.find_one({"username": username}):
                flash('El nombre de usuario ya existe.')
                return redirect(url_for('register'))
            
            hashed_password = generate_password_hash(password, method='sha256')
            mongo.db.users.insert_one({"username": username, "password": hashed_password})
            flash('Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect(url_for('login'))
        return render_template('layout.html', page='pagesLanding/register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            user = mongo.db.users.find_one({"username": username})
            if user and check_password_hash(user['password'], password):
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
        appointments_db = mongo.db.appointments.find({"username": session['username']})
        return render_template('layout.html', page='pagesCitas/citas.html', appointments=appointments_db)

    @app.route('/crear_cita', methods=['GET', 'POST'])
    @login_required
    def create_appointment():
        if request.method == 'POST':
            specialty = request.form['specialty']
            doctor = request.form['doctor']
            date = request.form['date']
            time = request.form['time']
            
            appointment = {
                'username': session['username'],
                'specialty': specialty,
                'doctor': doctor,
                'date': date,
                'time': time
            }
            
            mongo.db.appointments.insert_one(appointment)
            flash('Cita creada con éxito.')
            return redirect(url_for('appointments'))
        
        specialties_db = mongo.db.specialties.find()
        doctors_db = mongo.db.doctors.find()
        return render_template('layout.html', page='pagesCitas/create_appointment.html', specialties=specialties_db, doctors=doctors_db)

# Inicializamos las rutas
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
