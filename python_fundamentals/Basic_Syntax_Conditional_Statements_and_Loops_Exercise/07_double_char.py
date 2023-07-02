while True:
    cur_string = input()
    double_string = ''
    if cur_string == "End":
        break
    if cur_string != "SoftUni":
        for symbol in cur_string:
            double_string += symbol * 2
        print(double_string)
        