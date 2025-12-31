population = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())

if sum(population) / len(population) >= minimum_wealth:
    for i in range(len(population)):
        while population[i] < minimum_wealth:
            max_welth = max(population)
            index = population.index(max_welth)
            dif = minimum_wealth - population[i]

            if population[index] - dif >= minimum_wealth:
                population[i] = minimum_wealth
                population[index] -= dif
            else:
                population[i] += population[index] - minimum_wealth
                population[index] = minimum_wealth

    print(population)
else:
    print("No equal distribution possible")