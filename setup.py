import os
from flask import Flask, render_template, request, redirect, url_for, session, flash

# Simulamos una base de datos de usuarios con un diccionario
users_db = {}

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para manejar sesiones

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre_nosotros')
def about():
    return render_template('about.html')

@app.route('/servicios')
def services():
    return render_template('services.html')

@app.route('/usuarios')
def users():
    return render_template('users.html')

@app.route('/roles')
def roles():
    return render_template('roles.html')

@app.route('/registro', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users_db:
            flash('El nombre de usuario ya existe.')
            return redirect(url_for('register'))
        users_db[username] = password  # Almacenamos el usuario y su contraseña
        flash('Registro exitoso. Ahora puedes iniciar sesión.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users_db.get(username) == password:
            session['username'] = username  # Almacena el nombre de usuario en la sesión
            flash('Inicio de sesión exitoso.')
            return redirect(url_for('home'))
        flash('Nombre de usuario o contraseña incorrectos.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Elimina el nombre de usuario de la sesión
    flash('Has cerrado sesión.')
    return redirect(url_for('home'))

# Función para crear la estructura de la aplicación Flask
def create_flask_app_structure(base_path):
    # Crear la carpeta principal
    os.makedirs(base_path, exist_ok=True)

    # Crear el archivo principal de la aplicación
    app_file_content = '''from flask import Flask, render_template, request, redirect, url_for, session, flash

# Simulamos una base de datos de usuarios con un diccionario
users_db = {}

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para manejar sesiones

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre_nosotros')
def about():
    return render_template('about.html')

@app.route('/servicios')
def services():
    return render_template('services.html')

@app.route('/usuarios')
def users():
    return render_template('users.html')

@app.route('/roles')
def roles():
    return render_template('roles.html')

@app.route('/registro', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users_db:
            flash('El nombre de usuario ya existe.')
            return redirect(url_for('register'))
        users_db[username] = password  # Almacenamos el usuario y su contraseña
        flash('Registro exitoso. Ahora puedes iniciar sesión.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users_db.get(username) == password:
            session['username'] = username  # Almacena el nombre de usuario en la sesión
            flash('Inicio de sesión exitoso.')
            return redirect(url_for('home'))
        flash('Nombre de usuario o contraseña incorrectos.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Elimina el nombre de usuario de la sesión
    flash('Has cerrado sesión.')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
'''
    with open(os.path.join(base_path, 'app.py'), 'w') as f:
        f.write(app_file_content)

    # Crear la carpeta de plantillas
    templates_path = os.path.join(base_path, 'templates')
    os.makedirs(templates_path, exist_ok=True)

    # Crear archivos HTML para las plantillas
    template_files = {
        'home.html': '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Inicio</title>
</head>
<body>
    <h1>Bienvenido a la página de inicio</h1>
    <nav>
        <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/sobre_nosotros">Sobre Nosotros</a></li>
            <li><a href="/servicios">Servicios</a></li>
            <li><a href="/usuarios">Usuarios</a></li>
            <li><a href="/roles">Roles</a></li>
            <li><a href="/registro">Registro</a></li>
            <li><a href="/login">Iniciar Sesión</a></li>
            <li><a href="/logout">Cerrar Sesión</a></li>
        </ul>
    </nav>
</body>
</html>
''',
        'about.html': '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Sobre Nosotros</title>
</head>
<body>
    <h1>Sobre Nosotros</h1>
    <p>Información sobre nosotros.</p>
    <nav>
        <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/sobre_nosotros">Sobre Nosotros</a></li>
            <li><a href="/servicios">Servicios</a></li>
            <li><a href="/usuarios">Usuarios</a></li>
            <li><a href="/roles">Roles</a></li>
            <li><a href="/registro">Registro</a></li>
            <li><a href="/login">Iniciar Sesión</a></li>
            <li><a href="/logout">Cerrar Sesión</a></li>
        </ul>
    </nav>
</body>
</html>
''',
        'services.html': '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Servicios</title>
</head>
<body>
    <h1>Servicios</h1>
    <p>Lista de servicios que ofrecemos.</p>
    <nav>
        <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/sobre_nosotros">Sobre Nosotros</a></li>
            <li><a href="/servicios">Servicios</a></li>
            <li><a href="/usuarios">Usuarios</a></li>
            <li><a href="/roles">Roles</a></li>
            <li><a href="/registro">Registro</a></li>
            <li><a href="/login">Iniciar Sesión</a></li>
            <li><a href="/logout">Cerrar Sesión</a></li>
        </ul>
    </nav>
</body>
</html>
''',
        'users.html': '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Usuarios</title>
</head>
<body>
    <h1>Usuarios</h1>
    <p>Gestión de usuarios.</p>
    <nav>
        <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/sobre_nosotros">Sobre Nosotros</a></li>
            <li><a href="/servicios">Servicios</a></li>
            <li><a href="/usuarios">Usuarios</a></li>
            <li><a href="/roles">Roles</a></li>
            <li><a href="/registro">Registro</a></li>
            <li><a href="/login">Iniciar Sesión</a></li>
            <li><a href="/logout">Cerrar Sesión</a></li>
        </ul>
    </nav>
</body>
</html>
''',
        'roles.html': '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Roles</title>
</head>
<body>
    <h1>Roles</h1>
    <p>Gestión de roles.</p>
    <nav>
        <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/sobre_nosotros">Sobre Nosotros</a></li>
            <li><a href="/servicios">Servicios</a></li>
            <li><a href="/usuarios">Usuarios</a></li>
            <li><a href="/roles">Roles</a></li>
            <li><a href="/registro">Registro</a></li>
            <li><a href="/login">Iniciar Sesión</a></li>
            <li><a href="/logout">Cerrar Sesión</a></li>
        </ul>
    </nav>
</body>
</html>
''',
        'register.html': '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registro</title>
</head>
<body>
    <h1>Registro de Usuario</h1>
    <form method="POST">
        <label for="username">Nombre de Usuario:</label>
        <input type="text" id="username" name="username" required>
        <label for="password">Contraseña:</label>
        <input type="password" id="password" name="password" required>
        <button type="submit">Registrarse</button>
    </form>
    <nav>
        <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/sobre_nosotros">Sobre Nosotros</a></li>
            <li><a href="/servicios">Servicios</a></li>
            <li><a href="/usuarios">Usuarios</a></li>
            <li><a href="/roles">Roles</a></li>
            <li><a href="/login">Iniciar Sesión</a></li>
        </ul>
    </nav>
</body>
</html>
''',
        'login.html': '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Iniciar Sesión</title>
</head>
<body>
    <h1>Iniciar Sesión</h1>
    <form method="POST">
        <label for="username">Nombre de Usuario:</label>
        <input type="text" id="username" name="username" required>
        <label for="password">Contraseña:</label>
        <input type="password" id="password" name="password" required>
        <button type="submit">Iniciar Sesión</button>
    </form>
    <nav>
        <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/sobre_nosotros">Sobre Nosotros</a></li>
            <li><a href="/servicios">Servicios</a></li>
            <li><a href="/usuarios">Usuarios</a></li>
            <li><a href="/roles">Roles</a></li>
            <li><a href="/registro">Registro</a></li>
        </ul>
    </nav>
</body>
</html>
'''
    }

    # Crear archivos HTML para las plantillas
    for template_name, template_content in template_files.items():
        template_file_path = os.path.join(templates_path, template_name)
        with open(template_file_path, 'w') as f:
            f.write(template_content)

# Crear la aplicación en el directorio actual
create_flask_app_structure(os.path.join(os.getcwd(), 'my_flask_app'))

# Imprimir mensaje de éxito
print("Estructura de la aplicación Flask con gestión de usuarios creada exitosamente.")
print("Ejecuta 'python app.py' en la carpeta 'my_flask_app' para iniciar la aplicación.")
