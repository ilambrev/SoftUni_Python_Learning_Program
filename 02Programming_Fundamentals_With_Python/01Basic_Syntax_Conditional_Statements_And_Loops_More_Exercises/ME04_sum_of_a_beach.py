text = input().lower()

counter = 0

counter += text.count("Sand".lower())
counter += text.count("Water".lower())
counter += text.count("Fish".lower())
counter += text.count("Sun".lower())

print(counter)