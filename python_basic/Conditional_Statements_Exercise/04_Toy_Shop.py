PUZZLE_PRICE = 2.60
TALKING_TOYS_PRICE = 3.00
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_TOY_PRICE = 2.00

vacation_price = float(input())
puzzle_quantity = int(input())
talking_toy_quantity = int(input())
teddy_bear_quantity = int(input())
minion_quantity = int(input())
truck_toy_quantity = int(input())
total_price = PUZZLE_PRICE * puzzle_quantity + TALKING_TOYS_PRICE * talking_toy_quantity \
              + TEDDY_BEAR_PRICE * teddy_bear_quantity + MINION_PRICE * minion_quantity + TRUCK_TOY_PRICE * truck_toy_quantity
total_toy_quantity = puzzle_quantity + talking_toy_quantity + teddy_bear_quantity + minion_quantity + truck_toy_quantity
if total_toy_quantity >= 50:
    total_price = total_price * 0.75
total_price = total_price * 0.90

if total_price >= vacation_price:
    print(f"Yes! {total_price-vacation_price:.02f} lv left.")
else:
    print(f"Not enough money! {vacation_price - total_price:.02f} lv needed.")
