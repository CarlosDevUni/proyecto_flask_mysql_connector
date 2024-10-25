-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS flask_app_db 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Indicar que base de datos usamos
USE flask_app_db;

-- Crear una tabla
CREATE TABLE IF NOT EXISTS people (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    dni INT(8) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE    
);