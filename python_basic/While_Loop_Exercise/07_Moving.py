width_space = int(input())
length_space = int(input())
height_space = int(input())
space = width_space * length_space * height_space
command = ""
while space > 0 and command != "Done":
    command = input()
    if command != "Done":
        space -= int(command)
if space < 0:
    print(f"No more free space! You need {-space} Cubic meters more.")
else:
    print(f"{space} Cubic meters left.")

