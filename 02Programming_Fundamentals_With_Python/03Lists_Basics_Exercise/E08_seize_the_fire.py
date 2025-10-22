fire_levels = input().split("#")
water = int(input())
total_effort = 0
putted_out_cells = []
begin_of_line = "- "
new_line = "\n"

for fire_level in fire_levels:
    level, value = fire_level.split(" = ")
    value = int(value)
    is_value_valid = False

    if level == "High" and 81 <= value <= 125:
        is_value_valid = True
    elif level == "Medium" and 51 <= value <= 80:
        is_value_valid = True
    elif level == "Low" and 1 <= value <= 50:
        is_value_valid = True

    if is_value_valid and water >= value:
        water -= value
        putted_out_cells.append(value)
        total_effort += 0.25 * value

print("Cells:")

if putted_out_cells:
    print(f"{new_line.join([begin_of_line + str(value) for value in putted_out_cells])}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(putted_out_cells)}")