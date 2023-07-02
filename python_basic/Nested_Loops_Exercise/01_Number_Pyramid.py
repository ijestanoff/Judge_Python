number = int(input())
count = 0
column = 0
row = 0
while count < number:
    row += 1
    while column < row:
        count += 1
        column += 1
        print(count, end=" ")
        if count == number:
            break
    print("")
    column = 0
