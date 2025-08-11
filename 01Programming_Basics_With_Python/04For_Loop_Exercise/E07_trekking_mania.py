climbers_groups_count = int(input())

musala_climbers_count = 0
mont_blanc_climbers_count = 0
kilimanjaro_climbers_count = 0
k2_climbers_count = 0
everest_climbers_count = 0

climbers = 0

for _ in range(climbers_groups_count):
    group_members_count = int(input())
    climbers += group_members_count

    if group_members_count <= 5:
        musala_climbers_count += group_members_count
    elif group_members_count <= 12:
        mont_blanc_climbers_count += group_members_count
    elif group_members_count <= 25:
        kilimanjaro_climbers_count += group_members_count
    elif group_members_count <= 40:
        k2_climbers_count += group_members_count
    else:
        everest_climbers_count += group_members_count

print(f'{100 * (musala_climbers_count / climbers):.2f}%')
print(f'{100 * (mont_blanc_climbers_count / climbers):.2f}%')
print(f'{100 * (kilimanjaro_climbers_count / climbers):.2f}%')
print(f'{100 * (k2_climbers_count / climbers):.2f}%')
print(f'{100 * (everest_climbers_count / climbers):.2f}%')