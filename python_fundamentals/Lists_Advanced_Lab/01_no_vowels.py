text_entered = input()
no_vowels = [symbol for symbol in text_entered if symbol.lower() not in ['a', 'o', 'u', 'e', 'i']]
print(''.join(no_vowels))