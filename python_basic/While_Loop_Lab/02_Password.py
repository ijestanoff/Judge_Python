input_user = input()
input_pass = input()
entered_pass = ""
while entered_pass != input_pass:
    entered_pass = input()
print(f"Welcome {input_user}!")