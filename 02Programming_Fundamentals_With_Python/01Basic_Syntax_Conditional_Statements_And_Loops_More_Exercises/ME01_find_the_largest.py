number = input()

largest_number = ""
temp_number = number

while len(temp_number) > 0:
    max_digit_index = -1
    max_digit = -1

    for i in range(len(temp_number)):
        if int(temp_number[i]) > max_digit:
            max_digit = int(temp_number[i])
            max_digit_index = i
    
    largest_number += str(max_digit)
    temp_number = temp_number[:max_digit_index] + temp_number[max_digit_index+1:]

print(int(largest_number))