#!/usr/bin/python3
from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!", 200


@app.route("/data")
def data():
    return jsonify([key for key in users]), 200


@app.route("/status")
def status():
    return "OK", 200


@app.route("/users/<username>")
def show_user(username):
    user = users.get(username)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data:
        return "invalid data", 400

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    users[data["username"]] = {
        "username": data["username"],
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
