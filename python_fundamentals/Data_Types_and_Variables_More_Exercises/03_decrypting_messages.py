master_key = int(input())
lines_number = int(input())
for count in range(lines_number):
    symbol = input()
    symbol_ascii = ord(symbol)
    symbol_ascii += master_key
    print(chr(symbol_ascii), end="")
