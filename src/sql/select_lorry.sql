SELECT colours.colour, vehicle.tax_due_date, vehicle.service_due_date, lorries_and_pickups.cargo_capacity, lorries_and_pickups.cab_type 
FROM vehicle, lorries_and_pickups, colours
WHERE vehicle.number_plate = '?NUM_PLATE?'
AND vehicle.number_plate = lorries_and_pickups.number_plate
AND colours.colourID = vehicle.colour_id;