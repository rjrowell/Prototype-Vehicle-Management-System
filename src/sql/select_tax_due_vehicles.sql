SELECT vehicle.number_plate, vehicle_types.vehicle_type, colours.colour, vehicle.tax_due_date
FROM vehicle, vehicle_types, colours
WHERE vehicle.tax_due_date BETWEEN DATE('now') AND DATE('now','+30 days')
AND colours.colourID = vehicle.colour_id
AND vehicle_types.typeID = vehicle.vehicle_type;