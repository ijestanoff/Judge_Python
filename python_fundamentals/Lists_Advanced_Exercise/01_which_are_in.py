first_list = input().split(", ")
second_list = input().split(", ")
result_list = []
for first in first_list:
    for second in second_list:
        if first in second:
            result_list.append(first)
            break
print(result_list)

