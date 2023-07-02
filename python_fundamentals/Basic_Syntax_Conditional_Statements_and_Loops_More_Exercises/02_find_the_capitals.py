enter_string = input()
mylist = []
for number, symbol in enumerate(enter_string):
    if symbol.isupper():
        mylist.append(number)
print(mylist)
