cargo_number = int(input())
total_price = 0
total_mass = 0
bus_cargo = 0
truck_cargo = 0
train_cargo = 0
for count in range(0, cargo_number, 1):
    cargo_mass = int(input())
    if cargo_mass <= 3:
        total_price += 200 * cargo_mass
        bus_cargo += cargo_mass
    elif cargo_mass <= 11:
        total_price += 175 * cargo_mass
        truck_cargo += cargo_mass
    elif cargo_mass >= 12:
        total_price += 120 * cargo_mass
        train_cargo += cargo_mass
    total_mass += cargo_mass
average_price = total_price / total_mass
print(f"{average_price:.2f}")
print(f"{bus_cargo / total_mass * 100:.2f}%")
print(f"{truck_cargo / total_mass * 100:.2f}%")
print(f"{train_cargo / total_mass * 100:.2f}%")
