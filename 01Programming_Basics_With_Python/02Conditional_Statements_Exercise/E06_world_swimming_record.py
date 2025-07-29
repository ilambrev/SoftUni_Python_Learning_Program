from math import floor

record_time_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_1_meter = float(input())

delay_in_seconds = floor(distance_in_meters / 15) * 12.5

competitor_time_in_seconds = (distance_in_meters
                              * time_in_seconds_for_1_meter
                              + delay_in_seconds)

time_difference = record_time_in_seconds - competitor_time_in_seconds

if (time_difference > 0):
    print(f'Yes, he succeeded! The new world record is {competitor_time_in_seconds:.2f} seconds.')
else:
    print(f'No, he failed! He was {abs(time_difference):.2f} seconds slower.')