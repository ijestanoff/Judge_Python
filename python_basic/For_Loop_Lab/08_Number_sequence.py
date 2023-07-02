total_number = int(input())
min_number = 10000000000000000
max_number = -1000000000000000
for count in range(0, total_number, 1):
    number = int(input())
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
