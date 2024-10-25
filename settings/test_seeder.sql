-- Indicar que base de datos usamos
USE flask_app_db;

-- Borramos datos existentes en la tabla
DELETE FROM people;

/* Insertar datos de prueba */
INSERT INTO people (name, surname, dni, email) VALUES
('Ana', 'García', 11111111, 'ana@mail.com'),
('Juan', 'Perez', 22222222, 'juan@mail.com'),
('María', 'Smith', 33333333, 'maria@mail.com'),
('José', 'Gonzalez', 44444444, 'jose@mail.com');
