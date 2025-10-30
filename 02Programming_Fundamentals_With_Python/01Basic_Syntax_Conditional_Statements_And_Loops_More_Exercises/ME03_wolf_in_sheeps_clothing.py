animals = input().split(", ")

animal = animals[-1]
wolf_index = animals.index("wolf")

if animal == "wolf":
    print("Please go away and stop eating my sheep")
elif animal == "sheep":
    print(f"Oi! Sheep number {len(animals) - 1 - wolf_index}! You are about to be eaten by a wolf!")