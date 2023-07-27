sum_numbers = lambda first, second: first + second
subtract = lambda first, second: first - second


def add_and_subtract(first, second, third):
    return subtract(sum_numbers(first, second), third)


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))

