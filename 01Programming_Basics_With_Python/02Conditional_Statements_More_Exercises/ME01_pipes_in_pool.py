pool_volume_in_liters = int(input())
first_pipe_flow_rate_per_hour = int(input())
second_pipe_flow_rate_per_hour = int(input())
time_in_hours = float(input())

first_pipe_water_amount = first_pipe_flow_rate_per_hour * time_in_hours
second_pipe_water_amount = second_pipe_flow_rate_per_hour * time_in_hours

total_water_amount = first_pipe_water_amount + second_pipe_water_amount

difference = pool_volume_in_liters - total_water_amount

if difference >= 0:
    first_pipe_percentage = 100 * first_pipe_water_amount / total_water_amount
    second_pipe_percentage = 100 * second_pipe_water_amount / total_water_amount
    pool_filling_percentage = 100 * total_water_amount / pool_volume_in_liters
    print(f'The pool is {pool_filling_percentage:.2f}% full. Pipe 1: {first_pipe_percentage:.2f}%. Pipe 2: {second_pipe_percentage:.2f}%.')
else:
    print(f'For {time_in_hours:.2f} hours the pool overflows with {-difference:.2f} liters.')