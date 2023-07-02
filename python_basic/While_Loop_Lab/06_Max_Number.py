import sys
great_number = -sys.maxsize
while True:
    text_entered = input()
    if text_entered == "Stop":
        print(great_number)
        break
    number = int(text_entered)
    if number > great_number:
        great_number = number

