message = input()
non_numbers = []
numbers_list = []
result_list = []
take_flag = True
for symbol in message:
    if symbol.isnumeric():
        numbers_list.append(int(symbol))
    else:
        non_numbers.append(symbol)
load = numbers_list.pop(0)
while len(numbers_list) > 0 and len(non_numbers) > 0:
    if take_flag:
        if load > 0:
            result_list.append(non_numbers.pop(0))
            load -= 1
        if load == 0:
            load = numbers_list.pop(0)
            take_flag = False
    else:
        if load > 0:
            non_numbers.pop(0)
            load -= 1
        if load == 0:
            load = numbers_list.pop(0)
            take_flag = True
print("".join(result_list))
