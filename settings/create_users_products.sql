-- Indicar que base de datos usamos
USE flask_app_db;

-- Crear una tabla para usuarios de la api
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Crear una tabla para productos
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    price INT NOT NULL,
    id_user INT NOT NULL,
    CONSTRAINT point_of_a_person 
    FOREIGN KEY (id_user) 
    REFERENCES users (id)
    ON DELETE CASCADE 
    ON UPDATE CASCADE
);
