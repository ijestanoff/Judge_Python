number = int(input())
row_string = "*" * 2 * number + " " * number + "*" * 2 * number
print(row_string)
for row in range(number - 2):
    if row == int((number - 1) / 2 - 1):
        symbol = "|"
    else:
        symbol = " "
    row_string = "*" + (2 * number - 2) * "/" + "*" + symbol * number + "*" + (2 * number - 2) * "/" + "*"
    print(row_string)
row_string = "*" * 2 * number + " " * number + "*" * 2 * number
print(row_string)
