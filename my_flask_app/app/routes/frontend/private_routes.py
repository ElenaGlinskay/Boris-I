from flask import Blueprint, render_template

private_bp = Blueprint('private', __name__)

@private_bp.route('/dashboard')
def dashboard():
    return render_template('pages/dashboardPages/dashboard.html')

@private_bp.route('/usuarios')
def usuarios():
    return render_template('pages/dashboardPages/usuarios.html')

@private_bp.route('/roles')
def roles():
    return render_template('pages/dashboardPages/roles.html')
