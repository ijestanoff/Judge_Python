sheep_list = input().split(", ")
index = sheep_list.index('wolf')
list_length = len(sheep_list)
if index == list_length - 1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {list_length - index - 1}! You are about to be eaten by a wolf!")
