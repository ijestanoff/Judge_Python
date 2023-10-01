from math import floor
def center_point(x1, y1, x2, y2):
    if (abs(x1) ** 2 + abs(y1) ** 2) ** 0.5 <= (abs(x2) ** 2 + abs(y2) ** 2) ** 0.5:
        print(f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})")
    else:
        print(f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})")

def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    length_first = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5
    length_second = (abs(x3 - x4) ** 2 + abs(y3 - y4) ** 2) ** 0.5
    if length_first >= length_second:
        center_point(x1, y1, x2, y2)
    else:
        center_point(x3, y3, x4, y4)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
