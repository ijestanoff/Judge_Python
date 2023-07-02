number_of_strings = int(input())
for cnt in range(number_of_strings):
    cur_string = input()
    for symbol in cur_string:
        if symbol == "," or symbol == "." or symbol == "_":
            print(f"{cur_string} is not pure!")
            break
    else:
        print(f"{cur_string} is pure.")