# •	Бензин – 2.22 лева за един литър,
# •	Дизел – 2.33 лева за един литър
# •	Газ – 0.93 лева за литър
GASOLINE_PRICE = 2.22
DIESEL_PRICE = 2.33
AUTO_GAS_PRICE = 0.93
type_fuel = input()
fuel_amount = float(input())
card_availability = input()
if card_availability == "Yes":
    GASOLINE_PRICE -= 0.18
    DIESEL_PRICE -= 0.12
    AUTO_GAS_PRICE -= 0.08
if type_fuel == "Gasoline":
    fuel_volume = GASOLINE_PRICE * fuel_amount
elif type_fuel == "Diesel":
    fuel_volume = DIESEL_PRICE * fuel_amount
elif type_fuel == "Gas":
    fuel_volume = AUTO_GAS_PRICE * fuel_amount
if fuel_amount > 25:
    fuel_volume *= 0.90
elif fuel_amount >= 20:
    fuel_volume *= 0.92
print(f"{fuel_volume:.02f} lv.")

