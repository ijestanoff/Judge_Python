list_string = input().split(" ")
list_int = [int(x) for x in list_string]
remove_number = int(input())
for _ in range(remove_number):
    minimum = list_int[0]
    for count in range(len(list_int)):
        if list_int[count] < minimum:
            minimum = list_int[count]
    list_int.remove(minimum)
print(list_int[0], end="")
for count in range(1, len(list_int)):
    print(f", {list_int[count]}", end="")