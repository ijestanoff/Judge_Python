elements = input().split()
element_dic = {}
for element in elements:
    if element.lower() not in element_dic:
        element_dic[element.lower()] = 1
    else:
        element_dic[element.lower()] += 1

for key, value in element_dic.items():
    if value % 2 == 1:
        print(key, end=" ")
