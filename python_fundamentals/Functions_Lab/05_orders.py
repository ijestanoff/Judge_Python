def order(product, quantity):
    if product == "coffee":
        return quantity * 1.50
    elif product == "water":
        return quantity * 1.00
    elif product == "coke":
        return  quantity * 1.40
    elif product == "snacks":
        return  quantity * 2.00

product = input()
quantity = float(input())
print(f"{order(product,quantity):.2f}")
