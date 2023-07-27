number_list = input().split(", ")
print_list = []
for number in number_list:
    print_list.append(int(number))
for number in range(len(print_list) - 1, -1, -1):
    if print_list[number] == 0:
        print_list.append(print_list.pop(number))
print(print_list)
