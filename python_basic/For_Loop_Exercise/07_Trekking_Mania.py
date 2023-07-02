groups_number = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k2_pik = 0
everest = 0
total_elements = 0
for count in range(0, groups_number, 1):
    element = int(input())
    total_elements += element
    if element <= 5:
        musala += element
    elif element <= 12:
        monblan += element
    elif element <= 25:
        kilimandjaro += element
    elif element <= 40:
        k2_pik += element
    else:
        everest += element
print(f"{(musala/total_elements)*100:.2f}%")
print(f"{(monblan/total_elements)*100:.2f}%")
print(f"{(kilimandjaro/total_elements)*100:.2f}%")
print(f"{(k2_pik/total_elements)*100:.2f}%")
print(f"{(everest/total_elements)*100:.2f}%")
