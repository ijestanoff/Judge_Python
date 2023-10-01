products = {}
while True:
    command = input().split()
    if command[0] == "buy":
        break
    product, price, quantity = command
    price = float(price)
    quantity = int(quantity)
    if product not in products:
        products[product] = [price, quantity]
    else:
        old_quantity = products[product][1]
        products[product] = [price, old_quantity + quantity]

for product in products:
    amount = products[product][0] * products[product][1]
    print(f"{product} -> {amount:.2f}")
