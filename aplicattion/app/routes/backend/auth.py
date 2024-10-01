import jwt
import datetime
from flask import Blueprint, request, jsonify
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app import mongo, config

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.find_by_username(username)

    if user and check_password_hash(user['password'], password):
        token = jwt.encode({
            'username': user['username'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, config.Config.SECRET_KEY, algorithm='HS256')

        return jsonify({'token': token}), 200

    return jsonify({'message': 'Credenciales inválidas'}), 401
