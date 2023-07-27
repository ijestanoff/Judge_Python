number_list = input().split()
list_int = []
for number in number_list:
    list_int.append(int(number))
while True:
    command_list = input().split()
    if command_list[0] == "end":
        break
    if command_list[0] == "exchange":
        index = int(command_list[1])
        if index >= len(list_int) or index < 0:
            print("Invalid index")
        else:
            list_int = list_int[index + 1:] + list_int[:index + 1]
    if command_list[0] == "max":
        max_element = 0
        max_position = "No matches"
        if command_list[1] == "odd":
            for count in range(len(list_int)):
                if list_int[count] % 2 != 0:
                    if list_int[count] >= max_element:
                        max_element = list_int[count]
                        max_position = count
        elif command_list[1] == "even":
            for count in range(len(list_int)):
                if list_int[count] % 2 == 0:
                    if list_int[count] >= max_element:
                        max_element = list_int[count]
                        max_position = count
        print(max_position)
    if command_list[0] == "min":
        min_element = 99999999999
        min_position = "No matches"
        if command_list[1] == "odd":
            for count in range(len(list_int)):
                if list_int[count] % 2 != 0:
                    if list_int[count] <= min_element:
                        min_element = list_int[count]
                        min_position = count
        elif command_list[1] == "even":
            for count in range(len(list_int)):
                if list_int[count] % 2 == 0:
                    if list_int[count] <= min_element:
                        min_element = list_int[count]
                        min_position = count
        print(min_position)
    if command_list[0] == "first":
        first_even = []
        first_odd = []
        count = int(command_list[1])
        if count > len(list_int):
            print("Invalid count")
        elif command_list[2] == "even":
            for number in list_int:
                if number % 2 == 0:
                    first_even.append(number)
                    count -= 1
                    if count == 0:
                        break
            print(first_even)
        elif command_list[2] == "odd":
            for number in list_int:
                if number % 2 != 0:
                    first_odd.append(number)
                    count -= 1
                    if count == 0:
                        break
            print(first_odd)
    if command_list[0] == "last":
        last_even = []
        last_odd = []
        count = int(command_list[1])
        if count > len(list_int):
            print("Invalid count")
        elif command_list[2] == "even":
            for number in list_int:
                if number % 2 == 0:
                    last_even.append(number)
            while len(last_even) > count:
                last_even.pop(0)
            print(last_even)
        elif command_list[2] == "odd":
            for number in list_int:
                if number % 2 != 0:
                    last_odd.append(number)
            while len(last_odd) > count:
                last_odd.pop(0)
            print(last_odd)
print(list_int)

