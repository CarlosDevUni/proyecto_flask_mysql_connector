from flask import Flask, jsonify
from api.db.db_config import get_db_connection

app = Flask(__name__)

@app.route('/')
def test():
    return jsonify({"message" : "test ok"})



# @app.route('/people')
# def index():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM people")
#     data = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return jsonify(data)

import api.routes.person
