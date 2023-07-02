max_diff = 0
both_numbers = int(input())
last_sum = 0
first_number = int(input())
second_number = int(input())
last_sum = first_number + second_number
for number in range(both_numbers - 1):
    first_number = int(input())
    second_number = int(input())
    current_sum = first_number + second_number
    if current_sum != last_sum:
        diff = abs(current_sum - last_sum)
        if diff > max_diff:
            max_diff = diff
    last_sum = current_sum
if max_diff == 0:
    print(f"Yes, value={last_sum}")
else:
    print(f"No, maxdiff={max_diff}")

