number_list = input().split()
new_list = []
for number in number_list:
    new_list.append(abs(float(number)))
print(new_list)