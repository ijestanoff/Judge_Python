number = int(input())
four_num = 0
for special_number in range(1111, 10000):
    number_str = str(special_number)
    for symbol in number_str:
        if int(symbol) > 0:
            if number % int(symbol) == 0:
                four_num += 1
    if four_num == 4:
        print(special_number, end=" ")
    four_num = 0
