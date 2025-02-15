SELECT colours.colour, vehicle.tax_due_date, vehicle.service_due_date, van.cargo_capacity 
FROM vehicle, van, colours
WHERE vehicle.number_plate = '?NUM_PLATE?'
AND vehicle.number_plate = van.number_plate
AND colours.colourID = vehicle.colour_id;