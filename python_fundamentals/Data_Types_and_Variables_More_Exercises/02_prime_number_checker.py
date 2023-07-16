number = int(input())
for count in range(2,number):
    if number % count == 0:
        print("False")
        break
else:
    print("True")
