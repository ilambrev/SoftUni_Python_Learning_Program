countries = [country for country in input().split(", ")]
capitals = [capital for capital in input().split(", ")]

[print(f"{country} -> {capital}") for country, capital in dict(zip(countries, capitals)).items()]