-- script that creates a table users with attributes:
-- id, email, name
-- If the table already exists, the script should not fail


CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    PRIMARY KEY (id)
);
