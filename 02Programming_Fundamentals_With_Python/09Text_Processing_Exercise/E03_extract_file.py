file_path = input()

index = file_path.rindex("\\")
file_with_extension = file_path if index == -1 else file_path[index+1:]
file_name, file_extension = file_with_extension.split(".")

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")