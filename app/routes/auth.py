from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    
    if not name or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400
    
    user, error = AuthService.register_user(name, email, password)
    if error:
        return jsonify({'error': error}), 400
    
    return jsonify(user.to_dict()), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    token, error = AuthService.login_user(email, password)
    if error:
        return jsonify({'error': error}), 401
    
    return jsonify({'token': token}), 200

