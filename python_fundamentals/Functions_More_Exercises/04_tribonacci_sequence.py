def tribonacci_sequence(number):
    number1, number2, number3 = 0, 0, 1
    print("1", end=' ')
    for count in range(number-1):
        sum_numbers = number1 + number2 + number3
        print(sum_numbers, end=' ')
        number1 = number2
        number2 = number3
        number3 = sum_numbers


number = int(input())
tribonacci_sequence(number)
