people_list = input().split()
step = int(input())
number_people = []
for people in people_list:
    number_people.append(int(people))
people_list = []
index = -1
while len(number_people) > 0:
    index += step
    while index >= len(number_people):
        index -= len(number_people)
    people_list.append(number_people.pop(index))
    index -= 1
print("[", end="")
print(*people_list, sep=',', end="")
print("]")
