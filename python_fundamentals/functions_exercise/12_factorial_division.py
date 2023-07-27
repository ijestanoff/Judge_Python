def factorial_division(first, second):
    factorial_first, factorial_second = 1, 1
    for count in range(2, first + 1):
        factorial_first *= count
    for count in range(2, second + 1):
        factorial_second *= count
    print(f"{factorial_first / factorial_second:.2f}")


first_number = int(input())
second_number = int(input())
factorial_division(first_number, second_number)
