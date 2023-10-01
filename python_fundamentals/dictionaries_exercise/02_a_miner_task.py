metals = {}
while True:
    command = input()
    if command == "stop":
        break
    metal = command
    quantity = int(input())
    if metal not in metals:
        metals[metal] = 0
    metals[metal] += quantity

for key, val in metals.items():
    print(f"{key} -> {val}")