from api.db.db_config import get_db_connection, DBError
from api import app

class Product():
    schema = {
        "name": str,
        "price" : int
    }

    @classmethod
    def validate(cls,data):
        if data == None or type(data) != dict:
            return False
        # Control: data contiene todas las claves?
        for key in cls.schema:
            if key not in data:
                return False
            # Control: cada valor es del tipo correcto?
            if type(data[key]) != cls.schema[key]:
                return False
        return True
    
    # Constructor base (se tiene en cuenta el orden de las columnas en la base de datos!)
    def __init__(self, data):
        self._id = data[0]
        self._name = data[1]
        self._price = data[2]
        self._id_user = data[3]

    # Conversión a objeto JSON
    def to_json(self):
        return {
            "id": self._id,
            "name": self._name,
            "price": self._price,
            "id_user": self._id_user
        } 
    
    @classmethod
    def get_products_by_user(cls, id_user):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM products WHERE id_user = %s', (id_user,))
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        print(data)
        # Comprobar si se obtuvo algun registro
        if len(data) > 0:
            lista = []
            for fila in data:
                objeto = Product(fila).to_json()
                lista.append(objeto)
            return lista
    
        # Excepcion para indicar que no existe el recurso
        raise DBError("No existe el recurso solicitado")