from flask import Blueprint, request, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

users = {
    "test@uva.edu": {
        "password_hash": generate_password_hash("password123"),
        "name": "Jenny Schilling",
        "role": "Athlete"
    }
}

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = users.get(email)
    if not user or not check_password_hash(user["password_hash"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    session['user'] = {"email": email, "name": user["name"], "role": user["role"]}
    return jsonify({"message": "Logged in", "user": session["user"]})

@auth.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({"message": "Logged out"})

@auth.route('/current-user', methods=['GET'])
def current_user():
    user = session.get('user')
    if not user:
        return jsonify({"error": "Not logged in"}), 401
    return jsonify(user)
