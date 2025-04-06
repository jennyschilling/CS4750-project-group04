from flask import Blueprint, request, session, jsonify
from db_config import get_db_connection

data_route = Blueprint('data', __name__)

@data_route.route('/race-history')
def race_history():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM RaceResult;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(rows)