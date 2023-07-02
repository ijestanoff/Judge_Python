budget = float(input())
season = input()
car_class = ""
car_price = 0
car_type = ""
if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_price = budget * 0.35
        car_type = "Cabrio"
    elif season == "Winter":
        car_price = budget * 0.65
        car_type = "Jeep"
elif budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_price = budget * 0.45
        car_type = "Cabrio"
    elif season == "Winter":
        car_price = budget * 0.80
        car_type = "Jeep"
elif budget > 500:
    car_class = "Luxury class"
    car_price = budget * 0.90
    car_type = "Jeep"
print(car_class)
print(f"{car_type} - {car_price:.2f}")

