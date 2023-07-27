def palindrome(number):
    half_length = len(number) // 2
    if number[:half_length:] == number[-1:-(half_length+1):-1]:
        return True
    return False


list_numbers = input().split(", ")
for number in list_numbers:
    print(palindrome(number))
