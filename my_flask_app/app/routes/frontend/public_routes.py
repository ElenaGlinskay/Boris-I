from flask import Blueprint, render_template

public_bp = Blueprint('public', __name__)

@public_bp.route('/')
def index():
    return render_template('pages/landingPages/index.html')

@public_bp.route('/sobre_nosotros')
def sobre_nosotros():
    return render_template('pages/landingPages/sobre_nosotros.html')

@public_bp.route('/servicios')
def servicios():
    return render_template('pages/landingPages/servicios.html')
