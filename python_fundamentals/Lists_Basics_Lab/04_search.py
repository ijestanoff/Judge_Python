number = int(input())
filter_word = input()
list_string = []
filtered_list = []
for count in range(number):
    current_string = input()
    list_string.append(current_string)
    if filter_word in current_string:
        filtered_list.append(current_string)
print(list_string)
print(filtered_list)


