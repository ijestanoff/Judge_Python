number = int(input())
for row in range(number):
    for column in range(number):
        print(f"*", end="")
        if column != number - 1:
            print(f" ", end="")
    if row != number - 1:
        print("")
