stock = {}
while True:
    command = input().split(": ")
    if command[0] == "statistics":
        break
    product, quantity = command
    quantity = int(quantity)
    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

print("Products in stock:")
for k, v in stock.items():
    print(f"- {k}: {v}")
print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")