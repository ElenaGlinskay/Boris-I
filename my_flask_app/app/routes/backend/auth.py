from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user
from app import mongo

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = mongo.db.users.find_one({"username": username})

        if user and user['password'] == password:
            login_user(user)
            return redirect(url_for('private.dashboard'))  # Redirige al dashboard

    return render_template('pages/landingPages/login.html')
