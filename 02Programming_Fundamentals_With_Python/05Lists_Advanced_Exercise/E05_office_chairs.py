rooms_count = int(input())

free_chairs = 0
are_chairs_in_all_rooms_enough = True

for i in range(1, rooms_count + 1):
    chairs, visitors = input().split()
    difference = len(chairs) - int(visitors)

    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {i}")
        are_chairs_in_all_rooms_enough = False
    else:
        free_chairs += difference

if are_chairs_in_all_rooms_enough:
    print(f"Game On, {free_chairs} free chairs left")