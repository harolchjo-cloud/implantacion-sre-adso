from flask import Flask, jsonify
import mysql.connector
import os
import time
app = Flask(__name__)
def get_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "db"),
        user=os.environ.get("DB_USER", "root"),
        password="SuperClave123",
        database=os.environ.get("DB_NAME", "proyecto_db")
    )
@app.route("/")
def home():
    return jsonify({"status": "ok", "mensaje": "API funcionando correctamente"})
@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200
@app.route("/db-check")
def db_check():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        cursor.close()
        conn.close()
        return jsonify({"status": "ok", "mysql_version": version[0]})
    except Exception as e:
        return jsonify({"status": "error", "detalle": str(e)}), 500
if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")  # nosec B104 - necesario para exponer el servicio dentro del contenedor Docker
    app.run(host=host, port=5050)
