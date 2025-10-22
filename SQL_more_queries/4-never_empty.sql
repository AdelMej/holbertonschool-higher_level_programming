-- create the table id not null with a default id of 1
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256)
);
