def password_validator(password):
    is_valid = True
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    is_letters_digits = True
    number_digits = 0
    for char in password:
        if not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 or 48 <= ord(char) <= 57):
            is_letters_digits = False
        if 48 <= ord(char) <= 57:
            number_digits += 1
    if not is_letters_digits:
        print("Password must consist only of letters and digits")
        is_valid = False
    if number_digits < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


password = input()
password_validator(password)