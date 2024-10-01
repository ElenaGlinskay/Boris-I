from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
