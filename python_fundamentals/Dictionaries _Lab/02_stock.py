foods = input().split()
food_dic = {}

for index in range(0, len(foods), 2):
    food = foods[index]
    quantity = foods[index+1]
    food_dic[food] = int(quantity)

products = input().split()
for product in products:
    if product in food_dic.keys():
        print(f"We have {food_dic[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")