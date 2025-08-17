input_line = input()

while input_line != 'End':    
    destination = input_line
    budget = float(input())

    saved_money = 0.0

    while True:
        input_line = input()

        if input_line.replace(".", "").isnumeric():
            saved_money += float(input_line)
        else:
            if saved_money >= budget:
                print(f'Going to {destination}!')
            break