string_list = input().split(", ")
number_list = [int(number) for number in string_list]
index_list=[]
for index_of_number in range(len(number_list)):
    if number_list[index_of_number] % 2 == 0:
        index_list.append(index_of_number)
print(index_list)

# number_list = list(map(int, input().split(", ")))
# founds_indices_or_no = map(lambda x: x if number_list[x] % 2 == 0 else 'no', range(len(number_list)))
# even_indices = list(filter(lambda a: a !='no', founds_indices_or_no))
# print(even_indices)
