inherited_money = float(input())
money_left = inherited_money
year_to_live = int(input())
total_year = year_to_live - 1800
for cnt_year in range(0, total_year + 1, 1):
    if cnt_year % 2 == 0:
        money_left -= 12000
    else:
        money_left -= 12000 + (18 + cnt_year) * 50
if money_left >= 0:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    print(f"He will need {abs(money_left):.2f} dollars to survive.")
