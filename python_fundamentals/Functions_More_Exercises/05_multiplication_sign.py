def multiplication_sigh(number1, number2, number3):
    if number1 == 0 or number2 == 0 or number3 == 0:
        return 'zero'
    number_of_minus = 0
    if number1 < 0:
        number_of_minus += 1
    if number2 < 0:
        number_of_minus += 1
    if number3 < 0:
        number_of_minus += 1
    if number_of_minus == 3 or number_of_minus == 1:
        return 'negative'
    return 'positive'


number1 = int(input())
number2 = int(input())
number3 = int(input())
print(multiplication_sigh(number1, number2, number3))
