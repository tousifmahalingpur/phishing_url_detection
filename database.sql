CREATE DATABASE phishing_db;

USE phishing_db;

CREATE TABLE url_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(500),
    result VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
