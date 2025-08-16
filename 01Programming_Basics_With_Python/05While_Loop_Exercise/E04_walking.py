steps_goal = 10000

total_steps = 0
has_gabi_go_home = False

while True:
    input_line = input()

    if input_line == 'Going home':
        has_gabi_go_home = True
        continue

    steps = int(input_line)
    total_steps += steps

    if total_steps >= steps_goal or has_gabi_go_home:
        break

difference = total_steps - steps_goal

if difference >= 0:
    print('Goal reached! Good job!')
    print(f'{difference} steps over the goal!')
else:
    print(f'{abs(difference)} more steps to reach goal.')