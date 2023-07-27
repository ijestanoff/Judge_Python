card_list = input().split(" ")
number_of_shuffles = int(input())
split = int(len(card_list) / 2)
for count in range(number_of_shuffles):
    result_list = []
    for card in range(split):
        result_list.append(card_list[card])
        result_list.append(card_list[card+split])
    card_list = result_list
print(card_list)
