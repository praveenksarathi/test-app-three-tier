from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "testdb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS test_data (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            value TEXT NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route('/data', methods=['POST'])
def write_data():
    data = request.get_json()
    name = data.get("name")
    value = data.get("value")
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO test_data (name, value) VALUES (%s, %s)", (name, value))
    conn.commit()
    cur.close()
    conn.close()
    return "Data written", 201

@app.route('/data', methods=['GET'])
def read_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, value FROM test_data")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

@app.route('/data', methods=['DELETE'])
def delete_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM test_data")
    conn.commit()
    cur.close()
    conn.close()
    return "Data deleted", 200

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
