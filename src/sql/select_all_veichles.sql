SELECT veichle.number_plate, veichle_types.veichle_type, colours.colour
FROM veichle, veichle_types, colours
WHERE colours.colourID = veichle.colour_id
AND veichle_types.typeID = veichle.veichle_type;