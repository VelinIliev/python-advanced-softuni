number_of_plates = int(input())

parking_lot = set()

for car in range(number_of_plates):
    new = input().split(", ")
    action = new[0]
    plate = new[1]
    if action == "IN":
        parking_lot.add(plate)
    elif action == "OUT":
        parking_lot.remove(plate)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")