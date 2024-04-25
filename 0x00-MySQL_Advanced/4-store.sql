-- Initial
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;

CREATE TABLE IF NOT EXISTS items (
	name varchar(255) NOT NULL,
	quantity int NOT NULL DEFAULT 10
);

CREATE TABLE IF NOT EXISTS orders (
	item_name varchar(255) NOT NULL,
	number int not null
);

INSERT INTO items (name) VALUES ("appel"), ("pineapple"), ("pear");
