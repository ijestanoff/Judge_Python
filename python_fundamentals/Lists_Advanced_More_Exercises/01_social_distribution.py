population = list(map(int, input().split(", ")))
wealth = int(input())

no_equal = False
for people_index in range(len(population)):
    richest = max(population)
    richest_index = population.index(richest)
    if population[people_index] < wealth:
        difference = wealth - population[people_index]
        population[richest_index] -= difference
        if population[richest_index] < wealth:
            no_equal = True
            break
        population[people_index] = wealth

if no_equal:
    print("No equal distribution possible")
else:
    print(population)