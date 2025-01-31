CREATE TABLE veichle(number_plate varchar(8) PRIMARY KEY, veichle_type varchar(16), colour varchar(16), tax_due_date varchar(8), mot_due_date varchar(8));
CREATE TABLE car(number_plate varchar(8) PRIMARY KEY, number_of_seats INTEGER);
CREATE TABLE van(number_plate varchar(8) PRIMARY KEY, cargo_capacity INTEGER);
CREATE TABLE lorries_and_pickups(number_plate varchar(8) PRIMARY KEY, cargo_capacity INTEGER, cab_type varchar(8));

INSERT INTO veichle VALUES ('HC56XPQ', 'car', 'red', '05122025', '08112025');
INSERT INTO car VALUES ('HC56XPQ', 5);

INSERT INTO veichle VALUES ('HC62XAC', 'van', 'white', '05092025', '22112025');
INSERT INTO van VALUES ('HC62XAC', 15100);

INSERT INTO veichle VALUES ('QS52BCG', 'lorry', 'blue', '05072025', '17082025');
INSERT INTO lorries_and_pickups VALUES ('QS52BCG', 35000, 'sleeper');

INSERT INTO veichle VALUES ('BG70LKM', 'pickup', 'green', '05112025', '30092025');
INSERT INTO lorries_and_pickups VALUES ('BG70LKM', 1876, 'single');
