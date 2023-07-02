import decimal
change_money = float(input())
number_of_coins = 0
while change_money > 0:
    number_of_coins += 1
    if change_money >= 2:
        change_money -= 2
    elif change_money >= 1:
        change_money -= 1
    elif change_money >= 0.5:
        change_money -= 0.5
    elif change_money >= 0.2:
        change_money -= 0.2
    elif change_money >= 0.1:
        change_money -= 0.1
    elif change_money >= 0.05:
        change_money -= 0.05
    elif change_money >= 0.02:
        change_money -= 0.02
    elif change_money >= 0.01:
        change_money -= 0.01
    change_money = round(change_money,2)
print (number_of_coins)
