# •	Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
# •	Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;
# •	Всички останали са "unknown".
product = input()
product_type = "unknown"
if product == "banana" or product == "apple" or product == "kiwi" or product == "cherry" or product == "lemon" or product == "grapes":
    product_type = "fruit"
elif product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot":
    product_type = "vegetable"
print(product_type)
