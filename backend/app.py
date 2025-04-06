from flask import Flask, jsonify, session, Blueprint
from flask_cors import CORS
from auth import auth
import os
from data_routes import data_route

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app, supports_credentials=True)

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(data_route, url_prefix='/api')

@app.route('/')
def home():
    return jsonify({"message": "Backend is running"})

if __name__ == '__main__':
    app.run(debug=True)
