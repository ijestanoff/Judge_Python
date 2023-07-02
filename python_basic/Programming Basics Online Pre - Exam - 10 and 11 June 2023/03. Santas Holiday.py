room_for_one_person = 18.00
apartment = 25.00
president_apartment = 35.00

stay_days = int(input())
stay_days -= 1
type_room = str(input())
flag = str(input())
discount = 0
total_price = 0
if stay_days < 10:
    if type_room == "room for one person":
        discount = 0
    elif type_room == "apartment":
        discount = 0.3
    elif type_room == "president apartment":
        discount = 0.1
elif 10 <= stay_days <= 15:
    if type_room == "room for one person":
        discount = 0
    elif type_room == "apartment":
        discount = 0.35
    elif type_room == "president apartment":
        discount = 0.15
elif stay_days > 15:
    if type_room == "room for one person":
        discount = 0
    elif type_room == "apartment":
        discount = 0.5
    elif type_room == "president apartment":
        discount = 0.2
if type_room == "room for one person":
    total_price = room_for_one_person * stay_days
elif type_room == "apartment":
    total_price = apartment * stay_days
elif type_room == "president apartment":
    total_price = president_apartment * stay_days

total_price = total_price - total_price * discount
if flag == "positive":
    total_price = total_price + total_price * 0.25
elif flag == "negative":
    total_price = total_price - total_price * 0.1
print(f"{total_price:.2f}")

