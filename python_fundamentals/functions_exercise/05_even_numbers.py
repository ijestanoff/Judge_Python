def even_number(number):
    if number % 2 == 0:
        return True
    else:
        return False


list_numbers = input().split()
new_list = []
for number in list_numbers:
    new_list.append(int(number))

print(list(filter(even_number, new_list)))
