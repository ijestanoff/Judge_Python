number = int(input())
list_numbers = []
for count in range(number):
    current_number = int(input())
    list_numbers.append(current_number)
command = input()
for count in range(len(list_numbers) - 1, -1, -1):
    remove_action = False
    current_number = list_numbers[count]
    if command == "even":
        if current_number % 2 != 0:
            remove_action = True
    elif command == "odd":
        if current_number % 2 == 0:
            remove_action = True
    elif command == "negative":
        if current_number >= 0:
            remove_action = True
    elif command == "positive":
        if current_number < 0:
            remove_action = True
    if remove_action:
        list_numbers.remove(current_number)
print(list_numbers)
