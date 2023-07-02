lili_age = int(input())
laundry_price = float(input())
toy_price = int(input())
toy_sum = 0
lili_money = 0
for count in range(1,lili_age + 1,1):
    if count % 2 == 0:
        lili_money += 10 * count / 2
        lili_money -= 1
    else:
        toy_sum += toy_price
lili_money += toy_sum
if lili_money >= laundry_price:
    print(f"Yes! {lili_money-laundry_price:.2f}")
else:
    print(f"No! {laundry_price-lili_money:.2f}")
