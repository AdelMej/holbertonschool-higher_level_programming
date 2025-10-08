#!/usr/bin/python3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (
        create_access_token, jwt_required, get_jwt
)
from flask import Flask, jsonify, request

app = Flask(__name__)
app.url_map.strict_slashes = False
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "secret-key"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
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
    if user and check_password_hash(user["password"], password):
        token = create_access_token(
            identity=username,
            additional_claims={"role": user["role"]}
        )
        return jsonify(access_token=token)
    return jsonify(error="Unauthorized"), 401


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    user = get_jwt()
    if user["role"] != 'admin':
        return jsonify(error="Admin access required"), 403
    else:
        return "Admin Access: Granted", 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


"""
--- TOKEN ERROR HANDLERS ---
All must return 401 for unauthorized access
"""


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify(error="Unauthorized"), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify(error="Unauthorized"), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify(error="Unauthorized"), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify(error="Unauthorized"), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify(error="Unauthorized"), 401


if __name__ == "__main__":
    app.run()
