number_list = input().split()
message = input()
out_string = ""
for number_position in number_list:
    position = 0
    number = int(number_position)
    while number > 0:
        position += number % 10
        number = number // 10
    while position > len(message) - 1:
        position -= len(message)
    out_string += message[position]
    message = message[:position] + message[position+1:]
print(out_string)
