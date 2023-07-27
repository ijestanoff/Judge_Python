gifts_list = input().split(" ")
while True:
    command = input().split(" ")
    if command[0] == "No" and command[1] == "Money":
        break
    if "OutOfStock" in command:
        gift_remove = command[1]
        for count in range(len(gifts_list)):
            if gifts_list[count] == gift_remove:
                gifts_list[count] = "None"
    elif "Required" in command:
        gift_index = int(command[2])
        if 0 <= gift_index < len(gifts_list):
            gifts_list[gift_index] = command[1]
    elif "JustInCase" in command:
        gifts_list[-1] = command[1]
for gift in gifts_list:
    if gift != "None":
        print(gift, end=" ")
