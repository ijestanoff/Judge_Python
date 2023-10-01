elements = list(map(int, input().split()))
elements_sum = 0
while len(elements) > 0:
    index_to_remove = int(input())
    pop_element = True
    if index_to_remove < 0:
        amount = elements[0]
        elements[0] = elements[-1]
        pop_element = False
    elif index_to_remove >= len(elements):
        amount = elements[-1]
        elements[-1] = elements[0]
        pop_element = False
    else:
        amount = elements[index_to_remove]
    elements_sum += amount
    for index in range(len(elements)):
        if elements[index] <= amount:
            elements[index] += amount
        else:
            elements[index] -= amount
    if pop_element:
        elements.pop(index_to_remove)
print(elements_sum)
