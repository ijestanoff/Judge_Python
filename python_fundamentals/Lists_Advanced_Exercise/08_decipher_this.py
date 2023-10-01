secret_message = input().split()
for word in secret_message:
    if (word[:3:]).isnumeric():
        first_symbol = chr(int(word[:3:]))
        rest_text = word[3::]
    else:
        first_symbol = chr(int(word[:2:]))
        rest_text = word[2::]
    char_list = list(rest_text)
    char_list[0], char_list[-1] = char_list[-1], char_list[0]
    hole_text = first_symbol + "".join(char_list)
    print(hole_text, end = " ")
