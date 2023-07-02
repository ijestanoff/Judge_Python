vacation_money = float(input())
saved_money = float(input())
spend_count = 0
day_count = 0
while True:
    reaction_type = input()
    amount = float(input())
    day_count += 1
    if reaction_type == "spend":
        spend_count += 1
        saved_money -= amount
        if saved_money < 0:
            saved_money = 0
        if spend_count == 5:
            print("You can't save the money.")
            print(day_count)
            break
    elif reaction_type == "save":
        spend_count = 0
        saved_money += amount
    if saved_money >= vacation_money:
        print(f"You saved the money for {day_count} days.")
        break


