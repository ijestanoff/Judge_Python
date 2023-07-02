# Град	0 ≤ s ≤ 500 	500 < s ≤ 1 000	    1 000 < s ≤ 10 000	    s > 10 000
# Sofia	    5%	            7%	                8%	                    12%
# Varna	    4.5%	        7.5%	            10%	                    13%
# Plovdiv	5.5%	        8%	                12%	                    14.5%
city = input()
sells = float(input())
commission = 0
if 0 <= sells <= 500:
    if city == "Sofia":
        commission = 5
    elif city == "Varna":
        commission = 4.5
    elif city == "Plovdiv":
        commission = 5.5
elif 500 <= sells <= 1000:
    if city == "Sofia":
        commission = 7
    elif city == "Varna":
        commission = 7.5
    elif city == "Plovdiv":
        commission = 8
elif 1000 <= sells <= 10000:
    if city == "Sofia":
        commission = 8
    elif city == "Varna":
        commission = 10
    elif city == "Plovdiv":
        commission = 12
elif sells > 10000:
    if city == "Sofia":
        commission = 12
    elif city == "Varna":
        commission = 13
    elif city == "Plovdiv":
        commission = 14.5
if commission == 0:
    print("error")
else:
    amount = sells * commission / 100
    print(f"{amount:.02f}")
