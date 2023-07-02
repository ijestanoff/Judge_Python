month = int(input())
total_electricity = 0
water = 0
internet = 0
other = 0
average = 0
for number in range(month):
    electricity = float(input())
    total_electricity += electricity
    water += 20
    internet += 15
    other += (electricity + 35) * 1.2
print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
average = (total_electricity + water + internet + other) / month
print(f"Average: {average:.2f} lv")
