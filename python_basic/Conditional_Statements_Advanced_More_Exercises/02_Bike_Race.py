# Група	        trail	cross-country	downhill	road
# juniors	    5.50	8	            12.25	    20
# seniors	    7	    9.50	        13.75	    21.50
juniors_cyclist = int(input())
seniors_cyclist = int(input())
race_type = input()
juniors_price = 0
seniors_price = 0
if race_type == "trail":
    juniors_price = 5.5
    seniors_price = 7
elif race_type == "cross-country":
    juniors_price = 8
    seniors_price = 9.5
    if juniors_cyclist + seniors_cyclist >= 50:
        juniors_price *= 0.75
        seniors_price *= 0.75
elif race_type == "downhill":
    juniors_price = 12.25
    seniors_price = 13.75
elif race_type == "road":
    juniors_price = 20
    seniors_price = 21.5
sum = (juniors_price * juniors_cyclist + seniors_price * seniors_cyclist) * 0.95
print(f"{sum:.2f}")

