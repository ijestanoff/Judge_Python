number = int(input())
first_number = 0
second_number = 0
third_number = 0
first_number = number % 10
second_number = int((number % 100) / 10)
third_number = int(number / 100)
for first_symbol in range(1, first_number + 1):
    for second_symbol in range(1, second_number + 1):
        for third_symbol in range(1, third_number + 1):
            result = first_symbol * second_symbol * third_symbol
            print(f"{first_symbol} * {second_symbol} * {third_symbol} = {result};")
