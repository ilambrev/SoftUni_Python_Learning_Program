target_time_minutes = int(input())
target_time_seconds = int(input())
chute_length_meters = float(input())
hundred_meters_seconds = int(input())

target_time_seconds += target_time_minutes * 60

competitor_time_seconds = hundred_meters_seconds * chute_length_meters / 100
competitor_time_reduction = 2.5 * chute_length_meters / 120

competitor_time_seconds -= competitor_time_reduction

if competitor_time_seconds <= target_time_seconds:
    print('Marin Bangiev won an Olympic quota!')
    print(f'His time is {competitor_time_seconds:.3f}.')
else:
    difference = competitor_time_seconds - target_time_seconds
    print(f'No, Marin failed! He was {difference:.3f} second slower.')