from math import floor
def center_point(x1, y1, x2, y2):
    if (abs(x1) ** 2 + abs(y1) ** 2) ** 0.5 <= (abs(x2) ** 2 + abs(y2) ** 2) ** 0.5:
        print(f"({floor(x1)}, {floor(y1)})")
    else:
        print(f"({floor(x2)}, {floor(y2)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
center_point(x1, y1, x2, y2)
