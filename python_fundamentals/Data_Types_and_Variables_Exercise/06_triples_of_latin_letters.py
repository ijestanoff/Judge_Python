number = int(input())
for first_sym in range(number):
    for second_sym in range(number):
        for third_sym in range(number):
            print(f"{chr(97+first_sym)}{chr(97+second_sym)}{chr(97+third_sym)}")
