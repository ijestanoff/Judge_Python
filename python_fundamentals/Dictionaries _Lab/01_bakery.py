foods = input().split()
food_dic = {}

for index in range(0, len(foods), 2):
    food = foods[index]
    quantity = foods[index+1]
    food_dic[food] = int(quantity)

print(food_dic)