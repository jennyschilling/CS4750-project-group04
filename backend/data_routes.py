from flask import Blueprint, request, session, jsonify
from db_config import get_db_connection

data_route = Blueprint('data', __name__)

@data_route.route('/race-result')
def race_history():
    user = session.get("user")
    if not user:
        return jsonify({"error": "Unauthorized"}), 401

    user_id = user["user_id"]

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT e.event_name, m.location, m.meet_date, r.result, r.place
        FROM RaceResult r
        JOIN Event e ON r.event_id = e.event_id
        JOIN Meet m ON e.meet_id = m.meet_id
        WHERE r.athlete_id = %s;
    """, (user_id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()

    result_list = [
        {
            "event": row[0],
            "location": row[1],
            "date": row[2],
            "result": row[3],
            "place": row[4]
        } for row in rows
    ]

    return jsonify(result_list)

@data_route.route('/teams')
def get_teams():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Team;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(rows)