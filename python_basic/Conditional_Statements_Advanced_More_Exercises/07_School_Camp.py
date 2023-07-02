season = input() # “Winter”, “Spring” или “Summer”
children_type = input() #“boys”, “girls” или “mixed”
children_number = int(input())
sleeps_number = int(input())
price_per_sleep = 0
discount = 0
sport_type = ""
if season == "Winter":
    if children_type == "boys":
        price_per_sleep = 9.6
        sport_type = "Judo"
    elif children_type == "girls":
        price_per_sleep = 9.6
        sport_type = "Gymnastics"
    else:
        price_per_sleep = 10
        sport_type = "Ski"
elif season == "Spring":
    if children_type == "boys":
        price_per_sleep = 7.2
        sport_type = "Tennis"
    elif children_type == "girls":
        price_per_sleep = 7.2
        sport_type = "Athletics"
    else:
        price_per_sleep = 9.5
        sport_type = "Cycling"
elif season == "Summer":
    if children_type == "boys":
        price_per_sleep = 15
        sport_type = "Football"
    elif children_type == "girls":
        price_per_sleep = 15
        sport_type = "Volleyball"
    else:
        price_per_sleep = 20
        sport_type = "Swimming"
total_price = children_number * price_per_sleep * sleeps_number
if children_number >= 50:
    discount = 0.5
elif children_number >= 20:
    discount = 0.15
elif children_number >= 10:
    discount = 0.05
total_price *= 1 - discount
print(f"{sport_type} {total_price:.2f} lv.")
