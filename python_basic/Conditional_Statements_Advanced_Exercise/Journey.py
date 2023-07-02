budget = float(input())
season = input()
amount = 0
destination = ""
type_sleep = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        amount = budget * 0.3
        type_sleep = "Camp"
    elif season == "winter":
        amount = budget * 0.7
        type_sleep = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        amount = budget * 0.4
        type_sleep = "Camp"
    elif season == "winter":
        amount = budget * 0.8
        type_sleep = "Hotel"
elif budget > 1000:
    destination = "Europe"
    amount = budget * 0.9
    type_sleep = "Hotel"
print(f"Somewhere in {destination}")
print(f"{type_sleep} - {amount:.2f}")
