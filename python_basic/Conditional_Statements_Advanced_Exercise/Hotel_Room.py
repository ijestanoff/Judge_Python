# Май и октомври	                Юни и септември	                    Юли и август
# Студио - 50 лв./нощувка	        Студио - 75.20 лв./нощувка	        Студио - 76 лв./нощувка
# Апартамент - 65 лв./нощувка 	Апартамент - 68.70 лв./нощувка	    Апартамент - 77 лв./нощувка

# •	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# •	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# •	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# •	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление
apartment_price = 0
studio_price = 0
month = input()
sleeps = int(input())
if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if sleeps > 14:
        studio_price *= 0.7
    elif sleeps > 7:
        studio_price *= 0.95
elif month == "June" or month == "September":
    studio_price = 75.2
    apartment_price = 68.7
    if sleeps > 14:
        studio_price *= 0.8
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
if sleeps > 14:
    apartment_price *= 0.9
print(f"Apartment: {apartment_price * sleeps:.2f} lv.")
print(f"Studio: {studio_price * sleeps:.2f} lv.")
