command = ""
text_word = ""
n_symbol = False
c_symbol = False
o_symbol = False
while command != "End":
    command = input()
    if command != "End":
        if not c_symbol and command == "c":
            c_symbol = True
        elif not n_symbol and command == "n":
            n_symbol = True
        elif not o_symbol and command == "o":
            o_symbol = True
        else:
            if "A" <= command <= "Z" or "a" <= command <= "z":
                text_word += command
        if c_symbol and n_symbol and o_symbol:
            print(f"{text_word} ", end="")
            text_word = ""
            c_symbol = False
            o_symbol = False
            n_symbol = False
