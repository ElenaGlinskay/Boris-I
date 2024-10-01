from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

def init_routes(app, mongo, login_required):
    
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
    def specialities():
        return render_template('layout.html', page='pagesLanding/specialities.html')

    @app.route('/docs')
    def docs():
        # Filtra solo los médicos
        doctors = mongo.db.users.find({"role": "doctor"})  
        return render_template('layout.html', page='pagesDashboard/users/doctors.html', doctors=doctors)

    @app.route('/registro', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            role = request.form['role']  # Añadimos el campo para el rol
            
            # Verificamos si el usuario ya existe en la base de datos
            if mongo.db.users.find_one({"username": username}):
                flash('El nombre de usuario ya existe.')
                return redirect(url_for('register'))
            
            # Si no existe, se registra el nuevo usuario
            hashed_password = generate_password_hash(password)  # Hashea la contraseña
            mongo.db.users.insert_one({"username": username, "password": hashed_password, "role": role})  # Guarda en MongoDB
            flash('Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect(url_for('login'))
        return render_template('layout.html', page='pagesLanding/register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            user = mongo.db.users.find_one({"username": username})  # Busca el usuario en MongoDB
            if user and check_password_hash(user['password'], password):  # Verifica la contraseña
                session['username'] = username
                session['role'] = user['role']  # Guarda el rol en la sesión
                flash('Inicio de sesión exitoso.')
                return redirect(url_for('dashboard'))  # Redirige al dashboard
            flash('Nombre de usuario o contraseña incorrectos.')
        return render_template('layout.html', page='pagesLanding/login.html')

    @app.route('/logout')
    def logout():
        session.pop('username', None)  # Elimina la sesión
        session.pop('role', None)  # Elimina el rol de la sesión
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
        # Aquí puedes recuperar y mostrar roles de la base de datos si es necesario
        roles_db = mongo.db.users.distinct('role')  # Obtener roles únicos
        return render_template('layout.html', page='pagesDashboard/roles.html', roles=roles_db)
