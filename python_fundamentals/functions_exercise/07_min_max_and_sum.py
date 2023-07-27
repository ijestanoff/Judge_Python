list_numbers = input().split()
new_list = []
for number in list_numbers:
    new_list.append(int(number))
print(f"The minimum number is {min(new_list)}")
print(f"The maximum number is {max(new_list)}")
print(f"The sum number is: {sum(new_list)}")
