line_numbers = int(input())
total_sum = 0
for count in range(line_numbers):
    symbol = input()
    total_sum += ord(symbol)
print(f"The sum equals: {total_sum}")
