# •	1ви ред: X кв.м е лозето – цяло число в интервала [10 … 5000]
# •	2ри ред: Y грозде за един кв.м – реално число в интервала [0.00 … 10.00]
# •	3ти ред: Z нужни литри вино – цяло число в интервала [10 … 600]
# •	4ти ред: брой работници – цяло число в интервала [1 … 20]
from math import ceil
vineyard = int(input())
grapes_per_sqm = float(input())
wine_needed = int(input())
workers_number = int(input())
wine_produced = vineyard * grapes_per_sqm * 0.4 / 2.5
if wine_produced < wine_needed:
    print(f"It will be a tough winter! More {int(wine_needed-wine_produced)} liters wine needed.")
if wine_produced >= wine_needed:
    print(f"Good harvest this year! Total wine: {int(wine_produced)} liters.")
    print(f"{ceil(wine_produced-wine_needed)} liters left -> {ceil((wine_produced-wine_needed)/workers_number)} liters per person.")
