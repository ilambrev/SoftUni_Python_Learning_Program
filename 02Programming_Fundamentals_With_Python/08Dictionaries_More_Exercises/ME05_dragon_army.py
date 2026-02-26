default_health = 250
default_damage = 45
default_armor = 10

dragons = {}

for _ in range(int(input())):
    type, name, damage, health, armor = input().split()
    damage = default_damage if damage == "null" else int(damage)
    health = default_health if health == "null" else int(health)
    armor = default_armor if armor == "null" else int(armor)
    
    if type not in dragons:
        dragons[type] = {}
    
    if name not in dragons[type]:
        dragons[type][name] = [0, 0, 0]

    dragons[type][name][0] = damage
    dragons[type][name][1] = health
    dragons[type][name][2] = armor

for k, v in dragons.items():
    avg = [sum([stat[i] for stat in v.values()]) / len(v) for i in range(3)]
    v = {name: stat for name, stat in sorted(v.items(), key=lambda item: item[0])}

    print(f"{k}::({avg[0]:.2f}/{avg[1]:.2f}/{avg[2]:.2f})")
    print("\n".join(f"-{name} -> damage: {d}, health: {h}, armor: {a}" for name, (d, h, a) in v.items()))