budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price
loaf_price = flour_price + eggs_price + milk_price / 4
loaf_number = 0
colored_eggs = 0
while budget > loaf_price:
    budget -= loaf_price
    loaf_number += 1
    colored_eggs += 3
    if loaf_number % 3 == 0:
        colored_eggs -= loaf_number - 2
print(f"You made {loaf_number} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")