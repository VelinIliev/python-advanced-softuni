number_of_plates = int(input())

parking_lot = set()

for car in range(number_of_plates):
    action, plate = input().split(", ")
    if action == "IN":
        parking_lot.add(plate)
    elif action == "OUT":
        parking_lot.remove(plate)

if parking_lot:
    [print(car) for car in parking_lot]
else:
    print("Parking Lot is Empty")