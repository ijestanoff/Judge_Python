name_list = input().split(", ")
sorted_names = sorted(name_list, key=lambda x: (-len(x), x))
print(sorted_names)
