total_number = int(input())
sum_first = 0
sum_second = 0
for count in range(0, total_number*2, 1):
    number = int(input())
    if count < total_number:
        sum_first += number
    else:
        sum_second += number
if sum_first >= sum_second:
    diff = sum_first - sum_second
else:
    diff = sum_second - sum_first
if diff == 0:
    print(f"Yes, sum = {abs(sum_first)}")
else:
    print(f"No, diff = {abs(diff)}")
