def process_data(data_type, data):
    if data_type == "int":
        return int(data) * 2

    if data_type == "real":
        result = float(data) * 1.5
        return f"{result:.2f}"

    if data_type == "string":
        return f"${data}$"

data_type = input()
data = input()

print(process_data(data_type, data))