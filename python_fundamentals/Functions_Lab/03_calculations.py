def my_calculator(operator, num1, num2):
    return {
        'multiply': num1 * num2,
        'divide': int(num1 / num2),
        'subtract': num1 - num2,
        'add': num1 + num2
    }.get(operator, 'Invalid operator')

my_operator = input()
number1 = int(input())
number2 = int(input())
print(my_calculator(my_operator, number1, number2))

