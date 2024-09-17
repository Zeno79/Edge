import os

# Initialize a flag and list for sequence processing
in_sequence = False
files_to_process = []

def rename_file(file_path, new_name):
    # Implement your file renaming logic here
    print(f"Renaming '{file_path}' to '{new_name}'")
    os.rename(file_path, new_name)

def execute_command(command, file_path=None):
    global in_sequence
    global files_to_process

    if command == "startsequence":
        in_sequence = True
        files_to_process = []
        print("Starting sequence")
    elif command == "endsequence":
        if in_sequence:
            in_sequence = False
            print("Ending sequence")
            # Process all collected files in sequence
            for file in files_to_process:
                # Apply renaming logic or other actions
                rename_file(file, f"processed_{os.path.basename(file)}")
        else:
            print("Error: endsequence without startsequence")
    elif in_sequence:
        if file_path:
            files_to_process.append(file_path)
            print(f"Added '{file_path}' to sequence")
    else:
        if file_path:
            # Handle single file command
            rename_file(file_path, f"processed_{os.path.basename(file_path)}")

# Example usage
commands = [
    ("startsequence", None),
    ("", "file1.txt"),
    ("", "file2.txt"),
    ("endsequence", None),
]

for cmd, file in commands:
    execute_command(cmd, file)
