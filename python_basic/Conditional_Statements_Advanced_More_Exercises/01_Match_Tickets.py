# •	VIP – 499.99 лева.
# •	Normal – 249.99 лева.
# Запалянковците имат определен бюджет, а броят на хората в групата определя какъв процент от бюджета трябва да се
# задели за транспо
#   От 1 до 4 – 75% от бюджета.
# •	От 5 до 9 – 60% от бюджета.
# •	От 10 до 24 – 50% от бюджета.
# •	От 25 до 49 – 40% от бюджета.
# •	50 или повече – 25% от бюджета

budget = float(input())
category = input()
number_of_people = int(input())
transport = 0
if 1 <= number_of_people <= 4:
    transport = budget * 0.75
elif 5 <= number_of_people <= 9:
    transport = budget * 0.6
elif 10 <= number_of_people <= 24:
    transport = budget * 0.5
elif 25 <= number_of_people <= 49:
    transport = budget * 0.4
elif number_of_people >= 50:
    transport = budget * 0.25
money_left = budget - transport
if category == "VIP":
    ticket_price = 499.99
else:
    ticket_price = 249.99
money_for_tickets = ticket_price * number_of_people
if money_for_tickets > money_left:
    print(f"Not enough money! You need {money_for_tickets - money_left:.2f} leva.")
else:
    print(f"Yes! You have {money_left - money_for_tickets:.2f} leva left.")
