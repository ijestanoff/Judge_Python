sum_numbers = 0
number = int(input())
for _ in range(number):
    current_number = int(input())
    sum_numbers += current_number
print(f"{sum_numbers / number:.2f}")
