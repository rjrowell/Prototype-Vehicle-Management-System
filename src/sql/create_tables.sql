CREATE TABLE vehicle(number_plate varchar(8) PRIMARY KEY, vehicle_type INTEGER, colour_id INTEGER, tax_due_date DATE, service_due_date DATE);
CREATE TABLE car(number_plate varchar(8) PRIMARY KEY, number_of_seats INTEGER);
CREATE TABLE van(number_plate varchar(8) PRIMARY KEY, cargo_capacity INTEGER);
CREATE TABLE lorries_and_pickups(number_plate varchar(8) PRIMARY KEY, cargo_capacity INTEGER, cab_type varchar(8));
CREATE TABLE vehicle_types(typeID INTEGER PRIMARY KEY AUTOINCREMENT, vehicle_type varchar(16));
CREATE TABLE colours(colourID INTEGER PRIMARY KEY AUTOINCREMENT, colour varchar(16));

