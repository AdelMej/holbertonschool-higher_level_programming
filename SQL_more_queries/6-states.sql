-- create a database and a table for states with an auto incrementing id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states(
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL
);
