from api.db.db_config import get_db_connection, DBError

class Person():
    schema = {
        "name": str,
        "surname" : str,
        "email" : str,
        "dni" : int
    }

    @classmethod
    def validate(cls,data):
        if data == None or type(data) != dict:
            return False
        # Control: data contiene todas las claves?
        for key in Person.schema:
            if key not in data:
                return False
            # Control: cada valor es del tipo correcto?
            if type(data[key]) != Person.schema[key]:
                return False
        return True

    # Constructor base (se tiene en cuenta el orden de las columnas en la base de datos!)
    def __init__(self, data):
        self._id = data[0]
        self._name = data[1]
        self._surname = data[2]
        self._dni = data[3]
        self._email = data[4]

    # Conversión a objeto JSON
    def to_json(self):
        return {
            "id": self._id,
            "name": self._name,
            "surname": self._surname,
            "dni": self._dni,
            "email": self._email,
        }    
    
    @classmethod   
    def get_person_by_id(cls, id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM people WHERE id = {0}'.format(id))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        
        if cursor.rowcount > 0:
            return Person(data[0]).to_json()
        raise DBError("No existe el recurso solicitado")