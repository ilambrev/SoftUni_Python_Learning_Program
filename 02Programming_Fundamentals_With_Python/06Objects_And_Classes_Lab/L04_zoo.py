class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        current_species = []
        type = ""

        if species == "mammal":
            current_species = self.mammals
            type = "Mammals"
        elif species == "fish":
            current_species = self.fishes
            type = "Fishes"
        elif species == "bird":
            current_species = self.birds
            type = "Birds"
        return f"{type} in {self.name}: {', '.join(current_species)}\nTotal animals: {Zoo.__animals}"

zoo_name = input()
n = int(input())
my_zoo = Zoo(zoo_name)

for i in range(n):
    species, name = input().split()
    my_zoo.add_animal(species, name)

species = input()

print(my_zoo.get_info(species))