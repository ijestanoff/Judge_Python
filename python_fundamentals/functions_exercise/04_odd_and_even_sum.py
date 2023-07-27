def odd_and_even_sum(number):
    sum_odd = 0
    sum_even = 0
    while number > 0:
        if (number % 10) % 2 == 0:
            sum_even += number % 10
        else:
            sum_odd += number % 10
        number = number // 10
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


number = int(input())
print(odd_and_even_sum(number))
