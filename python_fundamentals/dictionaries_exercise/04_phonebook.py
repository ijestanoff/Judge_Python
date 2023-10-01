phonebook = {}
while True:
    command = input().split("-")
    if command[0].isnumeric():
        break
    name, number = command
    phonebook[name] = number

for count in range(int(command[0])):
    find = input()
    if find in phonebook:
        print(f"{find} -> {phonebook[find]}")
    else:
        print(f"Contact {find} does not exist.")
