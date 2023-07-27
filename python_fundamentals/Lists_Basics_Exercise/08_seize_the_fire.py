fires_list = input().split("#")
water = int(input())
print("Cells:")
effort = 0
for count in range(len(fires_list)):
    cells = fires_list[count].split(" ")
    cell_level = int(cells[2])
    cell_valid = (
            cells[0] == "High" and 81 <= cell_level <= 125 and water >= cell_level
            or cells[0] == "Medium" and 51 <= cell_level <= 80 and water >= cell_level
            or cells[0] == "Low" and 1 <= cell_level <= 50 and water >= cell_level
    )
    if cell_valid:
        print(f"- {cell_level}")
        water -= cell_level
        effort += cell_level * 0.25
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {effort * 4:.0f}")
