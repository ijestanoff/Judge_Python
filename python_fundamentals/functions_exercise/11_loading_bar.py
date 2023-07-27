def loading_bar(number):
    percent_sign = number // 10
    dot_sign = 10 - percent_sign
    if percent_sign == 10:
        return "100% Complete!\n[%%%%%%%%%%]"
    return f"{number}% [{percent_sign * '%'}{dot_sign * '.'}]\nStill loading..."


number = int(input())
print(loading_bar(number))
