number = int(input())
for up_part in range(1, number + 1):
    row_string = " " * (number - up_part) + "*" + " *" * (up_part - 1)
    print(row_string)
for down_part in range(number - 1, 0, -1):
    row_string = " " * (number - down_part) + "*" + " *" * (down_part - 1)
    print(row_string)


