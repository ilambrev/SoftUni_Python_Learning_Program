from math import ceil

movie_name = input()
movie_duration = int(input())
rest_duration = int(input())

lunch_duration = rest_duration / 8
recreation_duration = rest_duration / 4

needed_time = lunch_duration + recreation_duration + movie_duration

difference = rest_duration - needed_time

if difference >= 0:
    print(f"You have enough time to watch {movie_name} and left with {ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(abs(difference))} more minutes.")