# •	Опаковъчна хартия - 5.80 лв. за ролка
# •	Плат - 7.20 лв. за ролка
# •	Лепило - 1.20 лв. за литър

PAPER = 5.80
TEXTILE = 7.20
GLUE = 1.20

rolls_paper = int(input())
rolls_textile = int(input())
liters_glue = float(input())
discount = int(input()) / 100

total_sum = PAPER * rolls_paper + TEXTILE * rolls_textile + GLUE * liters_glue
total_sum = total_sum - total_sum * discount
print (f"{total_sum:.3f}")