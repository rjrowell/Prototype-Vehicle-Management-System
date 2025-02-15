SELECT colours.colour, vehicle.tax_due_date, vehicle.service_due_date, car.number_of_seats 
FROM vehicle, car, colours
WHERE vehicle.number_plate = '?NUM_PLATE?'
AND vehicle.number_plate = car.number_plate
AND colours.colourID = vehicle.colour_id;