first_string = input()
second_string = input()
last_string = first_string
for count in range(len(first_string)):
    left_part = second_string[:count+1]
    right_part = first_string[count+1:]
    whole_string = left_part + right_part
    if whole_string != last_string:
        print(whole_string)
        last_string = whole_string
