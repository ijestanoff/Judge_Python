from math import ceil
MAGNOLIAS_PRICE = 3.25
HYACINTHS_PRICE = 4.00
ROSE_PRICE = 3.50
CACTUS_PRICE = 8.00

magnolias_quantity = int(input())
hyacinths_quantity = int(input())
rose_quantity = int(input())
cactus_quantity = int(input())
present_price = float(input())
income = MAGNOLIAS_PRICE * magnolias_quantity + HYACINTHS_PRICE * hyacinths_quantity \
         + ROSE_PRICE * rose_quantity + CACTUS_PRICE * cactus_quantity
income_with_tax = income * 0.95
if income_with_tax >= present_price:
    print(f"She is left with {int(income_with_tax - present_price)} leva.")
else:
    print(f"She will have to borrow {ceil(present_price - income_with_tax)} leva.")
