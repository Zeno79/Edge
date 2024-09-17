import os

# Initialize a flag and list for sequence processing
in_sequence = False
files_to_process = []

def rename_file(file_path, new_name):
    # Check if the file exists before renaming
    if os.path.isfile(file_path):
        try:
            print(f"Renaming '{file_path}' to '{new_name}'")
            os.rename(file_path, new_name)
        except OSError as e:
            print(f"Error renaming file '{file_path}': {e}")
    else:
        print(f"File not found: '{file_path}'")

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
                new_name = f"processed_{os.path.basename(file)}"
                rename_file(file, new_name)
        else:
            print("Error: endsequence without startsequence")
    elif in_sequence:
        if file_path:
            files_to_process.append(file_path)
            print(f"Added '{file_path}' to sequence")
    else:
        if file_path:
            # Handle single file command
            new_name = f"processed_{os.path.basename(file_path)}"
            rename_file(file_path, new_name)

# Example usage
# Ensure these files exist or replace them with your test files
commands = [
    ("startsequence", None),
    ("", "file1.txt"),  # Ensure file1.txt exists in the working directory
    ("", "file2.txt"),  # Ensure file2.txt exists in the working directory
    ("endsequence", None),
]

for cmd, file in commands:
    execute_command(cmd, file)
    
