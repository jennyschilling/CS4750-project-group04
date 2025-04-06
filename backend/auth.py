from flask import Blueprint, request, session, jsonify
# from werkzeug.security import generate_password_hash, check_password_hash
from db_config import get_db_connection

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT user_id, first_name, last_name, dob, gender, password_hash, phone, role FROM Users WHERE email = %s", (email,))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if not user:
        return jsonify({"error": "Invalid email"}), 401

    user_id, first_name, last_name, dob, gender, password_hash, phone, role = user

    # TODO: need to use actual hashes for the passwords
    # if not check_password_hash(password_hash, password):
    #     return jsonify({"error": "Incorrect password"}), 401
    if password_hash != password:
        return jsonify({"error": "Incorrect password"}), 401

    session['user'] = {
        "user_id": user_id,
        "email": email,
        "name": f"{first_name} {last_name}",
        "role": role,
        "dob": dob,
        "gender": gender,
        "phone": phone
    }

    return jsonify({"message": "Logged in", "user": session["user"]})