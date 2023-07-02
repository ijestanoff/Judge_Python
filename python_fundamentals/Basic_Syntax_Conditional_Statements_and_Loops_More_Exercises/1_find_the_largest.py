number = input()
find_replace = True
while find_replace:
    find_replace = False
    for count in range(len(number) - 1):
        part1 = number[:count]
        part2 = number[count + 1:count + 2]
        part3 = number[count:count + 1]
        part4 = number[count + 2:]
        if part3 < part2:
            find_replace = True
            number = part1 + part2 + part3 + part4
print(number)
