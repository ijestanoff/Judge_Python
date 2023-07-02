budget = int(input())
total = 0
while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    total += int(command)
    if total > budget:
        print("You went in overdraft!")
        break
