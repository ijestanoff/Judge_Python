beach = input().upper()
appear = 0
for number in range(len(beach)-2):
    if beach[number:number+4] == "SAND" or beach[number:number+4] == "FISH" or \
            beach[number:number+3] == "SUN" or beach[number:number+5] == "WATER":
        appear += 1
print(appear)

