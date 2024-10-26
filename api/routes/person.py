from api import app
from api.models.person import Person
from flask import jsonify

@app.route('/persons/<int:id>', methods = ['GET'])
def get_person_by_id(id):
    try:
        person = Person.get_person_by_id(id)
        return jsonify( person ), 200
    except Exception as e:
        return jsonify( {"message": e.args[0]} ), 400