def rounding(number):
    return round(number)

list_numbers = input().split()
new_numbers = []
for number in list_numbers:
    new_numbers.append(rounding(float(number)))
print(new_numbers)
