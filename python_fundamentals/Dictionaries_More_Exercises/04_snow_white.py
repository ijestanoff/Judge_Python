dwarfs = {}
number = 0
while True:
    command = input().split(" <:> ")
    if command[0] == "Once upon a time":
        break
    dwarf_name, dwarf_hat_color, dwarf_physics = command[0], command[1], int(command[2])
    dwarfs_nam_col = dwarf_hat_color + "<>" + dwarf_name
    if dwarfs_nam_col not in dwarfs:
        dwarfs[dwarfs_nam_col] = dwarf_physics
    else:
        if dwarf_physics > dwarfs[dwarfs_nam_col]:
            dwarfs[dwarfs_nam_col] = dwarf_physics

dwarfs_inx = {}
for key, val in dwarfs.items():
    color, name = key.split("<>")
    number_str = ''
    if number < 10:
        number_str = "0"
    number_str += str(number)
    new_key = color+"<>"+number_str+"<>"+name
    dwarfs_inx[new_key] = val
    number += 1

print(dwarfs_inx)
dwarfs = dict(sorted(dwarfs_inx.items(), key=lambda x: (-x[1], x[0])))
for color, physics in dwarfs.items():
    col, number, name = color.split("<>")
    print(f"({col}) {name} <-> {physics}")
