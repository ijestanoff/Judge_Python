divisor = int(input())
boundary = int(input())
for count in range(boundary, divisor - 1, -1):
    if count % divisor == 0:
        print(count)
        break