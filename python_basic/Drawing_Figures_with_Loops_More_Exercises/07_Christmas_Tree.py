number = int(input())
for row in range(1, number + 2):
    row_string = " " * (number - row + 1) + "*" * (row - 1) + " |"
    if row > 1:
        row_string += " " + "*" * (row - 1)
    print(row_string)