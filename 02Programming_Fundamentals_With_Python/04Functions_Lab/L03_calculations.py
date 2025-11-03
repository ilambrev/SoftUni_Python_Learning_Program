def calculate(operator, first_operand, second_operand):
    result = 0

    if operator == "multiply":
        result = first_operand * second_operand
    elif operator == "divide":
        result = first_operand / second_operand
    elif operator == "add":
        result = first_operand + second_operand
    elif operator == "subtract":
        result = first_operand - second_operand

    return int(result)

operator = input()
first_operand = int(input())
second_operand = int(input())

print(calculate(operator, first_operand, second_operand))