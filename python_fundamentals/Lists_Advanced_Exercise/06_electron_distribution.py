electron_number = int(input())
electron_list = []
order = 1
while electron_number > 0:
    electron = 2 * order ** 2
    if electron <= electron_number:
        electron_list.append(electron)
        electron_number -= electron
    else:
        electron_list.append(electron_number)
        electron_number = 0
    order += 1
print(electron_list)