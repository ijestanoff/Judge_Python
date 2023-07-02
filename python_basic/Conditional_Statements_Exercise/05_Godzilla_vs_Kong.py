# Ред 1.	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2.	Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3.	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

film_budget = float(input())
supernumerary_quantity = int(input())
supernumerary_clothing = float(input())
decor_price = film_budget * 0.10
if supernumerary_quantity > 150:
    supernumerary_clothing *= 0.90
supernumerary_amount = supernumerary_quantity * supernumerary_clothing
real_budget = decor_price + supernumerary_amount
if real_budget > film_budget:
    print(f"Not enough money!\nWingard needs {real_budget-film_budget:.02f} leva more.")
else:
    print(f"Action!\nWingard starts filming with {film_budget-real_budget:.02f} leva left.")

