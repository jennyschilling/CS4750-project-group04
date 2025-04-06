from flask import Blueprint, request, session, jsonify
from db_config import get_db_connection

data_route = Blueprint('data', __name__)

@data_route.route('/race-result')
def race_history():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM RaceResult;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(rows)

@data_route.route('/teams')
def get_teams():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Team;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(rows)