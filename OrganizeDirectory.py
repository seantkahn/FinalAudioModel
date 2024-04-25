#!/usr/bin/python
import os
import shutil

def organize_files_by_initial_letter(directory):
    # Create directories for each letter if they don't exist
    for char in range(ord('A'), ord('Z')+1):
        os.makedirs(os.path.join(directory, chr(char)), exist_ok=True)

    # List all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file in files:
        # Check if the first character is a letter and determine its uppercase form
        if file[0].isalpha():
            initial_letter = file[0].upper()
            # Construct the source and destination paths
            src_path = os.path.join(directory, file)
            dest_path = os.path.join(directory, initial_letter, file)
            # Move the file to the appropriate directory
            shutil.move(src_path, dest_path)
        else:
            # If the initial character is not a letter, we'll just print a message
            print(f"Skipping file {file} as it does not start with a letter.")

# Specify the directory to organize
directory = 'Data7'
organize_files_by_initial_letter(directory)
