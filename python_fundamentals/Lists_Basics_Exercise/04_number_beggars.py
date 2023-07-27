list_numbers = input().split(", ")
beggars = int(input())
list_beggars = []
for count in range(beggars):
    list_beggars.append(0)
    for sum_beggar in range(count, len(list_numbers), beggars):
        list_beggars[count] += int(list_numbers[sum_beggar])
print(list_beggars)
