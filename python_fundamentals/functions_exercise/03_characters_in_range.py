def char_in_range(first_char, second_char):
    string_chars = ""
    for char in range(ord(first_char)+1, ord(second_char)):
        string_chars += chr(char) + ' '
    return string_chars

first = input()
second = input()
print(char_in_range(first, second))
