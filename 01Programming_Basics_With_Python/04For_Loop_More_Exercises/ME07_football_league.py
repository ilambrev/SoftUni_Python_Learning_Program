stadium_capacity = int(input())
fan_count = int(input())

sector_a_count = 0
sector_b_count = 0
sector_v_count = 0
sector_g_count = 0

for _ in range(fan_count):
    sector = input()

    if sector == 'A':
        sector_a_count += 1
    elif sector == 'B':
        sector_b_count += 1
    elif sector == 'V':
        sector_v_count += 1
    elif sector == 'G':
        sector_g_count += 1

sector_a_percentage = 100 * sector_a_count / fan_count
sector_b_percentage = 100 * sector_b_count / fan_count
sector_v_percentage = 100 * sector_v_count / fan_count
sector_g_percentage = 100 * sector_g_count / fan_count
stadium_filling = 100 * fan_count / stadium_capacity

print(f'{sector_a_percentage:.2f}%')
print(f'{sector_b_percentage:.2f}%')
print(f'{sector_v_percentage:.2f}%')
print(f'{sector_g_percentage:.2f}%')
print(f'{stadium_filling:.2f}%')