parking = {}
number = int(input())
for count in range(number):
    command = input().split()
    name = command[1]
    if command[0] == "register":
        plate = command[2]
        if name in parking:
            print(f"ERROR: already registered with plate number {parking[name]}")
        else:
            parking[name] = plate
            print(f"{name} registered {plate} successfully")
    else:
        if name in parking:
            del parking[name]
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for name, plate in parking.items():
    print(f"{name} => {plate}")

