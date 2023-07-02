# Сезон	            Хризантеми	    Рози	        Лалета
# Пролет / Лято	    2.00 лв./бр.	4.10 лв./бр.	2.50 лв./бр.
# Есен / Зима	    3.75 лв./бр.	4.50 лв./бр.	4.15 лв./бр.
#
# •	На първия ред е броят на закупените хризантеми – цяло число в интервала [0 ... 200]
# •	На втория ред е броят на закупените рози – цяло число в интервала [0 ... 200]
# •	На третия ред е броят на закупените лалета – цяло число в интервала [0 ... 200]
# •	На четвъртия ред е посочен сезона – [Spring, Summer, Аutumn, Winter]
# •	На петия ред е посочено дали денят е празник – [Y – да / N - не]

chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2
    roses_price = 4.1
    tulips_price = 2.5
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15
if holiday == "Y":
    chrysanthemums_price *= 1.15
    roses_price *= 1.15
    tulips_price *= 1.15
# •	За закупени повече от 7 лалета през пролетта – 5% от цената на целият букет.
# •	За закупени 10 или повече рози през зимата – 10% от цената на целият букет.
# •	За закупени повече от 20 цветя общо през всички сезони – 20% от цената на целият букет.
total = chrysanthemums_price * chrysanthemums + roses_price * roses + tulips_price * tulips
if season == "Spring" and tulips > 7:
    total *= 0.95
elif season == "Winter" and roses >= 10:
    total *= 0.9
if chrysanthemums + roses + tulips > 20:
    total *= 0.8
total += 2
print (f"{total:.2f}")

