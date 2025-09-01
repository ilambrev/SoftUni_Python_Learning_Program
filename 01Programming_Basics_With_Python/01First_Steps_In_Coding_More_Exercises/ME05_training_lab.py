hall_length = float(input())
hall_width = float(input())

corridor_width = 1.0
lost_places = 3

hall_sits = int((hall_length // 1.2)
                * ((hall_width - corridor_width) // 0.7)
                - lost_places)

print(hall_sits)