cake_width = int(input())
cake_length = int(input())
number_of_peaces = cake_length * cake_width
command = ""
while number_of_peaces > 0 and command != "STOP":
    command = input()
    if command != "STOP":
        number_of_peaces -= int(command)
if number_of_peaces < 0:
    print(f"No more cake left! You need {-number_of_peaces} pieces more.")
else:
    print(f"{number_of_peaces} pieces are left.")

