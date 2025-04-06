import psycopg2
import os

def get_db_connection():
    conn = psycopg2.connect(
        host="bastion.cs.virginia.edu",
        port="5432",
        database="group04",
        user="group04",
        password="B8daV3E5"
    )
    return conn