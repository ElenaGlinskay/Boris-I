# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_session import Session
from datetime import datetime
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# Configuración de MongoDB
app.config['MONGO_URI'] = 'mongodb+srv://fanoro1945:fanoro1945@cluster0.j7bgf.mongodb.net/ThesesIniaf?retryWrites=true&w=majority'
app.config['SECRET_KEY'] = 'your_secret_key'  # Cambia esto a una clave secreta más segura
app.config['SESSION_TYPE'] = 'filesystem'

# Inicializa PyMongo y otras extensiones
mongo = PyMongo(app)
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
        user = {
            'email': form.email.data,
            'password': hashed_password,
            'role': form.role.data
        }
        mongo.db.users.insert_one(user)
        flash('Usuario registrado correctamente', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.users.find_one({'email': form.email.data})
        if user and bcrypt.check_password_hash(user['password'], form.password.data):
            session['user_id'] = str(user['_id'])
            session['role'] = user['role']
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
        cita = {
            'paciente_id': ObjectId(data['paciente_id']),
            'medico_id': ObjectId(data['medico_id']),
            'especialidad_id': data['especialidad_id'],
            'fecha': datetime.fromisoformat(data['fecha']),
            'estado': "Pendiente"
        }
        mongo.db.citas.insert_one(cita)
        flash('Cita creada', 'success')
        return redirect(url_for('manage_citas'))
    citas = mongo.db.citas.find()
    return render_template('citas.html', citas=citas)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('role', None)
    flash('Has cerrado sesión', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
