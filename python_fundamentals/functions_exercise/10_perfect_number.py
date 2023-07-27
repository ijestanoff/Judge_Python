def perfect_number(number):
    sum_digits = 0
    for count in range(1,number):
        if number % count == 0:
            sum_digits += count
    if sum_digits == number:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())
print(perfect_number(number))
