number = int(input())
symbol = ""
for row in range(number):
    for column in range(number):
        symbol = "-"
        if column == 0 or column == number - 1:
            symbol = "|"
            if row == 0 or row == number - 1:
                symbol = "+"
        print(f"{symbol}", end="")
        if column != number - 1:
            print(f" ", end="")
    if row != number - 1:
        print("")
