number_of_wagons = int(input())
train_list = [0] * number_of_wagons
while True:
    command = input().split()
    if command[0] == "End":
        print(train_list)
        break

    if command[0] == "add":
        train_list[-1] += int(command[1])
    else:
        index = int(command[1])
        people = int(command[2])
    if command[0] == "insert":
        train_list[index] += people
    if command[0] == "leave":
        train_list[index] -= people
