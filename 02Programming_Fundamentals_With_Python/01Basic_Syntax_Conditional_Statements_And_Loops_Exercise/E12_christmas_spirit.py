decorations_quantity = int(input())
days_left = int(input())

money_to_spend = 0
spirit_points = 0

ornament_set_price = 2
ornament_set_points = 5
tree_skirt_price = 5
tree_skirt_points = 3
tree_garland_price = 3
tree_garland_points = 10
tree_lights_price = 15
tree_lights_points = 17

for day in range(1, days_left + 1):
    if day % 11 == 0:
        decorations_quantity += 2

    if day % 2 == 0:
        money_to_spend += decorations_quantity * ornament_set_price
        spirit_points += ornament_set_points

    if day % 3 == 0:
        money_to_spend += decorations_quantity * (tree_skirt_price + tree_garland_price)
        spirit_points += tree_skirt_points + tree_garland_points

    if day % 5 == 0:
        money_to_spend += decorations_quantity * tree_lights_price
        spirit_points += tree_lights_points

    if day % 3 == 0 and day % 5 == 0:
        spirit_points += 30

    if day % 10 == 0:
        money_to_spend += tree_skirt_price + tree_garland_price + tree_lights_price
        spirit_points -= 20

if days_left % 10 == 0:
    spirit_points -= 30

print(f'Total cost: {money_to_spend}')
print(f'Total spirit: {spirit_points}')