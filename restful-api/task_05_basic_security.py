#!/usr/bin/python3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask import Flask, jsonify, request

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "secret-key"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    if username not in users:
        return None

    user = users[username]
    if (check_password_hash(user["password"], password)):
        return username


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if not user:
        return jsonify(message="401 Unauthorized"), 401

    if check_password_hash(user["password"], password):
        token = create_access_token(identity=username)
        return jsonify(access_token=token)
    else:
        return jsonify(message="401 Unauthorized"), 401


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    user = get_jwt_identity()
    user = users[user]
    if user["role"] != 'admin':
        return "403 Forbidden", 403
    else:
        return "Admin Access Granted", 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


if __name__ == "__main__":
    app.run(debug=True)
