def add_and_subtract(first_num, second_num, third_num):
    def sum_numbers(first_num, second_num):
        return first_num + second_num

    def subtract(first_num, second_num, third_num):
        return sum_numbers(first_num, second_num) - third_num

    return subtract(first_num, second_num, third_num)

first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))