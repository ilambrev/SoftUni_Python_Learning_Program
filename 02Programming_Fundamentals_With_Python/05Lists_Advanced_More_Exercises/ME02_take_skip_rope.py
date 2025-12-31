from string import digits

input_string = input()

numbers_list = [int(number) for number in input_string if number in digits]
letters_list = [letter for letter in input_string if letter not in digits]

take_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 == 0]
skip_list = [numbers_list[i] for i in range(len(numbers_list)) if not i % 2 == 0]

result_string = ""

start_index = 0

for i in range(len(take_list)):
    result_string += "".join(letters_list[start_index:start_index + take_list[i]])
    start_index += take_list[i] + skip_list[i]

print(result_string)