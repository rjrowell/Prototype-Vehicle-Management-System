SELECT vehicle_types.vehicle_type
FROM vehicle, vehicle_types
WHERE vehicle_types.typeID = vehicle.vehicle_type
AND vehicle.number_plate = ?;