target_quantity = 250
materials = {
    "shards": {"item": "Shadowmourne", "quantity": 0},
    "fragments": {"item": "Valanyr", "quantity": 0},
    "motes": {"item": "Dragonwrath", "quantity": 0}
}
junk = {}
legendary_item_obtained = False

while not legendary_item_obtained:
    meterials_data = input().split()
    for i in range(0, len(meterials_data), 2):
        quantity = int(meterials_data[i])
        material = meterials_data[i+1].lower()

        if material in materials:
            materials[material]["quantity"] += quantity

            if materials[material]["quantity"] >= target_quantity:
                materials[material]["quantity"] -= target_quantity
                legendary_item_obtained = True
                print(f"{materials[material]['item']} obtained!")
                break
        else:
            if material not in junk:
                junk[material] = 0

            junk[material] += quantity

[print(f"{key}: {value['quantity']}") for key, value in materials.items()]
[print(f"{key}: {value}") for key, value in junk.items()]


# Old task condition for output:
#
# On the first line, print the obtained item in the format: {Legendary item} obtained!
# On the next three lines, print the remaining key materials in descending order by quantity
#   If two key materials have the same quantity, print them in alphabetical order
# On the final several lines, print the junk items in alphabetical order
#   All materials are printed in format {material}: {quantity}
#   The output should be lowercase, except for the first letter of the legendary
#
# Solution for output according to the old condition
#
# materials_sorted = {k: v for k, v in sorted(materials.items(), key=lambda item: (-item[1]["quantity"], item[0]))}
# junk_sorted = {k: v for k, v in sorted(junk.items(), key=lambda item: item[0])}
#
# [print(f"{key}: {value['quantity']}") for key, value in materials_sorted.items()]
# [print(f"{key}: {value}") for key, value in junk_sorted.items()]