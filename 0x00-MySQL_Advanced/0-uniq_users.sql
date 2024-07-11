-- Creates a table with unique users.
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email CACHAR(255) NOT NULL UNIQUE,
    name VACHAR(255)
);