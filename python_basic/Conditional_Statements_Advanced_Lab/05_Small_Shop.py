# град / продукт	coffee	water	beer	sweets	peanuts
# Sofia	             0.50	0.80	1.20	1.45	1.60
# Plovdiv	        0.40	0.70	1.15	1.30	1.50
# Varna 	        0.45	0.70	1.10	1.35	1.55

product = input()
city = input()
quantity = float(input())
price = 0
if product == "coffee":
    if city == "Sofia":
        price = 0.50
    elif city == "Plovdiv":
        price = 0.40
    elif city == "Varna":
        price = 0.45
if product == "water":
    if city == "Sofia":
        price = 0.80
    elif city == "Plovdiv":
        price = 0.70
    elif city == "Varna":
        price = 0.70
if product == "beer":
    if city == "Sofia":
        price = 1.2
    elif city == "Plovdiv":
        price = 1.15
    elif city == "Varna":
        price = 1.10
if product == "sweets":
    if city == "Sofia":
        price = 1.45
    elif city == "Plovdiv":
        price = 1.30
    elif city == "Varna":
        price = 1.35
if product == "peanuts":
    if city == "Sofia":
        price = 1.60
    elif city == "Plovdiv":
        price = 1.50
    elif city == "Varna":
        price = 1.55
price *= quantity
print (price)



