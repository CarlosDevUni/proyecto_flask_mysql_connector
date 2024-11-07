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
    
@app.route('/persons', methods = ['GET'])
def get_all_persons():
    try:
        people = Person.get_all_persons()
        return jsonify( people ), 200
    except Exception as e:
        return jsonify( {"message": e.args[0]} ), 400