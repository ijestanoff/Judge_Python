budget = float(input())
season = input()
location = ""
hotel_type = ""
vacation_price = 0
if budget <= 1000:
    hotel_type = "Camp"
    if season == "Summer":
        location = "Alaska"
        vacation_price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        vacation_price = budget * 0.45
elif budget <= 3000:
    hotel_type = "Hut"
    if season == "Summer":
        location = "Alaska"
        vacation_price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        vacation_price = budget * 0.60
elif budget > 3000:
    hotel_type = "Hotel"
    if season == "Summer":
        location = "Alaska"
        vacation_price = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        vacation_price = budget * 0.90
print(f"{location} - {hotel_type} - {vacation_price:.2f}")
