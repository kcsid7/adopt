DROP DATABASE IF EXISTS adopt_db;
CREATE DATABASE adopt_db;

\c adopt_db

DROP TABLE IF EXISTS pets;
CREATE TABLE pets 
(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    photo_url TEXT,
    age INTEGER,
    notes TEXT,
    available BOOLEAN NOT NULL DEFAULT TRUE
)

INSERT INTO pets
(name, species, age, available) 
VALUES
('Pet1', 'Pet1', 10, 'Yes'),
('Pet2', 'Pet2', 1, 'Yes'),
('Pet3', 'Pet3', 3, 'No'),
('Pet4', 'Pet4', 5, 'Yes'),
('Pet5', 'Pet5', 8, 'No');