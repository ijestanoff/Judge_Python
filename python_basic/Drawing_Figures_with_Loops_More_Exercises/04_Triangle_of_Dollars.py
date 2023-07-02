number = int(input())
for row in range(number):
    for column in range(row + 1):
        print(f"$", end="")
        if column != row:
            print(f" ", end="")
    if row != number - 1:
        print("")
