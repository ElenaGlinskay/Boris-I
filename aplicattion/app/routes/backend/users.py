from flask import Blueprint, request, jsonify
from app.models.user import User
from werkzeug.security import generate_password_hash

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = list(mongo.db.users.find())
    return jsonify(users), 200

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    username = data['username']
    password = generate_password_hash(data['password'])
    role = data['role']
    User.create_user(username, password, role)
    return jsonify({'message': 'Usuario creado exitosamente'}), 201
