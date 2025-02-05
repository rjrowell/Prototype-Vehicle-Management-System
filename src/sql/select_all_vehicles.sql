SELECT vehicle.number_plate, vehicle_types.vehicle_type, colours.colour
FROM vehicle, vehicle_types, colours
WHERE colours.colourID = vehicle.colour_id
AND vehicle_types.typeID = vehicle.vehicle_type;