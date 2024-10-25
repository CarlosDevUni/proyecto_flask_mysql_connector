-- Usuario en localhost --
-- Crear un nuevo usuario con una contraseña segura
CREATE USER 'flask_user_name'@'localhost' IDENTIFIED BY 'flask_user_password';

-- Conceder todos los privilegios en la base de datos 
GRANT ALL PRIVILEGES ON flask_app_db.* TO 'flask_user_name'@'localhost' WITH GRANT OPTION;

-- Aplicar los cambios de privilegios (no es obligatorio en versiones modernas de MySQL)
-- FLUSH PRIVILEGES;

-- Verificar los privilegios del nuevo usuario
SHOW GRANTS FOR 'flask_user_name'@'localhost';

-- Usuario en 127.0.0.1 -- (Esto permite acceder tanto con localhost como la dirección IPv4)
-- Crear un nuevo usuario con una contraseña segura
CREATE USER 'flask_user_name'@'127.0.0.1' IDENTIFIED BY 'flask_user_password';

-- Conceder todos los privilegios en la base de datos 
GRANT ALL PRIVILEGES ON flask_app_db.* TO 'flask_user_name'@'127.0.0.1' WITH GRANT OPTION;

-- Aplicar los cambios de privilegios (no es obligatorio en versiones modernas de MySQL)
-- FLUSH PRIVILEGES;

-- Verificar los privilegios del nuevo usuario
SHOW GRANTS FOR 'flask_user_name'@'127.0.0.1';