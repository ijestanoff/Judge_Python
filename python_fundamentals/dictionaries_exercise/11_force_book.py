force_book = {}
while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        side_member = command.split(" | ")
        side, member = side_member
        has_member = False
        for force in force_book:
            if member in force_book[force]:
                has_member = True
        if side not in force_book and not has_member:
            force_book[side] = []
            force_book[side].append(member)
        elif side in force_book and not has_member:
            force_book[side].append(member)

    if "->" in command:
        member_side = command.split(" -> ")
        member, side = member_side
        has_member = False
        find_force = ''
        for force in force_book:
            if member in force_book[force]:
                has_member = True
                find_force = force
        if has_member:
            force_book[find_force].remove(member)
            if side not in force_book:
                force_book[side] = []
            force_book[side].append(member)
        elif side in force_book and not has_member:
            force_book[side].append(member)
        elif side not in force_book and not has_member:
            force_book[side] = []
            force_book[side].append(member)
        print(f"{member} joins the {side} side!")

for side, lists in force_book.items():
    if len(lists) > 0:
        print(f"Side: {side}, Members: {len(lists)}")
        for member in force_book[side]:
            print(f"! {member}")
