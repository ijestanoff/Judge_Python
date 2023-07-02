# •	Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
# •	Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
# •	Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# •	Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му и дължината на височината към нея
from math import pi
figure = input()
if figure == "square" :
    side = float(input())
    area = side ** 2
elif figure == "rectangle":
    length = float(input())
    width = float(input())
    area = length * width
elif figure == "circle":
    radius = float(input())
    area = pi * radius ** 2
elif figure == "triangle":
    height = float(input())
    base = float(input())
    area = height * base / 2
print (f"{area:.3f}")

