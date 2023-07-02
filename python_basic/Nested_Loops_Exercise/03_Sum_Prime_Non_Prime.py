sum_prime = 0
sum_non_prime = 0
while True:
    command = input()
    if command == "stop":
        break
    current_number = int(command)
    if current_number < 0:
        print ("Number is negative.")
    else:
        it_is_prime = True
        for number in range(2,current_number):
            if current_number % number == 0:
                it_is_prime = False
        if it_is_prime:
            sum_prime += current_number
        else:
            sum_non_prime += current_number
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
