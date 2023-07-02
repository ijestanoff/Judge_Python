stay_days = int(input())
type_of_room = input()
rating = input()
price = 0
sleeps = stay_days - 1
# 	"room for one person" – 18.00 лв за нощувка
# 	"apartment" – 25.00 лв за нощувка
# 	"president apartment" – 35.00 лв за нощувка
if type_of_room == "room for one person":
    price = 18
elif type_of_room == "apartment":
    price = 25
    if sleeps < 10:
        price *= 0.7
    elif sleeps <= 15:
        price *= 0.65
    else:
        price *= 0.5
elif type_of_room == "president apartment":
    price = 35
    if sleeps < 10:
        price *= 0.9
    elif sleeps <= 15:
        price *= 0.85
    else:
        price *= 0.8
if rating == "positive":
    price *= 1.25
else:
    price *= 0.9
print(f"{sleeps * price:.2f}")


