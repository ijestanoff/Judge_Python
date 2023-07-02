fruit = input()
size_set = input()
numbers_set = int(input())
price = 0
if fruit == "Watermelon":
    if size_set == "small":
        price = 2*56
    elif size_set == "big":
        price = 5*28.70
elif fruit == "Mango":
    if size_set == "small":
        price = 2*36.66
    elif size_set == "big":
        price = 5*19.60
elif fruit == "Pineapple":
    if size_set == "small":
        price = 2*42.1
    elif size_set == "big":
        price = 5*24.8
elif fruit == "Raspberry":
    if size_set == "small":
        price = 2*20
    elif size_set == "big":
        price = 5*15.2
price *= numbers_set
if 400 <= price <= 1000:
    price = price - price * 0.15
elif price > 1000:
    price /= 2
print(f"{price:.2f} lv.")