input_data = input().split()

input_line = input()

while not input_line == "3:1":
    parts = input_line.split()

    if parts[0] == "merge":
        start_index = int(parts[1]) if int(parts[1]) >= 0 else 0
        end_index = int(parts[2]) if int(parts[2]) < len(input_data) else len(input_data) - 1
        result = []
        
        input_data[start_index:end_index+1] = ["".join(input_data[start_index:end_index+1])]

    if parts[0] == "divide":
        index = int(parts[1])
        partitions = int(parts[2])

        partition_len = int(len(input_data[index]) / partitions)
        sub_list = []

        for i in range(0, partitions):
            if i == partitions - 1:
                sub_list.append(input_data[index][i*partition_len:])
            else:    
                sub_list.append(input_data[index][i*partition_len:(i*partition_len)+partition_len])

        input_data[index:index+1] = sub_list

    input_line = input()

print(" ".join(input_data))