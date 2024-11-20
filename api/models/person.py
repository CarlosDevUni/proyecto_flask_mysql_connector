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
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM people WHERE id = {0}'.format(id))
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        print(data)
        # Comprobar si se obtuvo algun registro
        if len(data) > 0:
            return Person(data[0]).to_json()
    
        # Excepcion para indicar que no existe el recurso
        raise DBError("No existe el recurso solicitado")
    
    @classmethod   
    def get_all_persons(cls):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM people')
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        print(data)
        # Comprobar si se obtuvo algun registro
        if len(data) > 0:
            lista = []
            for fila in data:
                objeto = Person(fila).to_json()
                lista.append(objeto)
            return lista
    
        # Excepcion para indicar que no existe el recurso
        raise DBError("No existe el recurso solicitado")
    
    @classmethod
    def create_person(cls,data):
        if not cls.validate(data):
            raise DBError("Campos/valores inválidos")
        
        connection = get_db_connection()
        cursor = connection.cursor()

        """ Control si existe el email indicado """
        email = data["email"]
        cursor.execute('SELECT * FROM people WHERE email = %s', (email,))
        row = cursor.fetchone()
        if row:
            raise DBError("Email ya registrado")
        
        """ Control si existe el dni indicado """
        dni = data["dni"]
        cursor.execute('SELECT * FROM people WHERE dni = %s', (dni,))
        row = cursor.fetchone()

        if row is not None:
            raise DBError("Dni ya registrado")
        
        """ acceso a BD -> INSERT INTO """    
        name = data["name"]
        surname = data["surname"]
        cursor.execute('INSERT INTO people (name, surname, dni, email) VALUES (%s, %s, %s, %s)', (name, surname, dni, email))
        connection.commit()

        """ obtener el id del registro creado """
        cursor.execute('SELECT LAST_INSERT_ID()')
        row = cursor.fetchone()
        id = row[0]

        # Recuperar el objeto completo
        cursor.execute('SELECT * FROM people WHERE id = %s', (id, ))
        nuevo = cursor.fetchone()
        cursor.close()
        connection.close()
        print(nuevo)
        return Person(nuevo).to_json()
    

    @classmethod
    def update_person(cls,id,data):
        if not cls.validate(data):
            raise DBError("Campos/valores inválidos")
        
        connection = get_db_connection()
        cursor = connection.cursor()

        """ Control si existe el recurso """
        cursor.execute("SELECT * FROM people WHERE id = %s", (id, ))
        row = cursor.fetchone()
        if row is None:
            raise DBError("No existe el recurso solicitado")

        """ Control si existe el email indicado en otra persona """
        email = data["email"]
        cursor.execute("SELECT id FROM people WHERE email = %s AND id != %s", (email, id))
        row = cursor.fetchone()
        if row is not None:
            raise DBError("Email ya registrado por otra persona")
        
        """ Control si existe el dni indicado en otra persona """
        dni = data["dni"]
        cursor.execute("SELECT id FROM people WHERE dni = %s AND id != %s", (dni, id))
        row = cursor.fetchone()
        if row is not None:
            raise DBError("Dni ya registrado por otra persona")
        
        """ acceso a BD -> UPDATE - SET """    
        name = data["name"]
        surname = data["surname"]
        cursor.execute('UPDATE people SET name = %s, surname = %s, dni = %s, email = %s WHERE id = %s', (name, surname, dni, email, id))
        connection.commit()

        # Recuperar el objeto completo
        cursor.execute('SELECT * FROM people WHERE id = %s', (id, ))
        actualizado = cursor.fetchone()
        cursor.close()
        connection.close()
        print(actualizado)
        return Person(actualizado).to_json()
    
    @classmethod   
    def delete_person(cls, id):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM people WHERE id = %s', (id, ))
        connection.commit()
        rowcount = cursor.rowcount
        print(rowcount)
        cursor.close()
        connection.close()
        if rowcount > 0:
            return {"id elemento elinado": id}
    
        # Excepcion para indicar que no existe el recurso
        raise DBError("No existe el recurso solicitado")