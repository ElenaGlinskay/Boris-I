from flask import Blueprint, render_template, request
from app import mongo

roles_bp = Blueprint('roles', __name__)

@roles_bp.route('/roles', methods=['GET'])
def get_roles():
    roles = list(mongo.db.roles.find())
    return jsonify(roles), 200

@roles_bp.route('/roles', methods=['POST'])
def create_role():
    role_name = request.json['name']
    mongo.db.roles.insert_one({"name": role_name})
    return jsonify({'message': 'Rol creado exitosamente'}), 201
