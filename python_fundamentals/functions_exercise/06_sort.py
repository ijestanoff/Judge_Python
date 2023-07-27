list_numbers = input().split()
new_list = []
for number in list_numbers:
    new_list.append(int(number))
sorted_list = sorted(new_list)
print(sorted_list)


