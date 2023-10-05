text = input()
text_dic = {}
for symbol in text:
    if symbol not in text_dic:
        text_dic[symbol] = 0
    text_dic[symbol] += 1
for key, val in text_dic.items():
    if key != " ":
        print(f"{key} -> {val}")

# test