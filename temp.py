# Test opening a file
file_name = "temp.txt"

try:
    with open(file_name, 'r') as file:
        print(f"File '{file_name}' opened successfully!")
        print("Here are the first few lines of the file:\n")
        for i, line in enumerate(file):
            if i >= 5:  # Show only the first 5 lines
                break
            print(line.strip())
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except PermissionError:
    print(f"Error: Permission denied to open the file '{file_name}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
