total_number = int(input())
sum_first = 0
sum_second = 0
for count in range(0, total_number, 1):
    number = int(input())
    if count % 2 == 0:
        sum_first += number
    else:
        sum_second += number
if sum_first >= sum_second:
    diff = sum_first - sum_second
else:
    diff = sum_second - sum_first
if diff == 0:
    print("Yes")
    print(f"Sum = {abs(sum_first)}")
else:
    print("No")
    print(f"Diff = {abs(diff)}")
