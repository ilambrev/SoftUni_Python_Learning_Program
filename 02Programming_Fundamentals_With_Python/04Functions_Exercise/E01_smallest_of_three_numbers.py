def find_smallest_number(first_num, second_num, third_num):
    nums = [first_num, second_num, third_num]

    return min(nums)

first_num = int(input())
second_num = int(input())
third_num = int(input())

print(find_smallest_number(first_num, second_num, third_num))