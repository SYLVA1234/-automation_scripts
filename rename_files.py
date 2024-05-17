import os

def rename_files(directory, old_extension, new_extension):
    for filename in os.listdir(directory):
        if filename.endswith(old_extension):
            new_filename = filename.replace(old_extension, new_extension)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")

# Example usage:
# Rename all .txt files in the directory "my_directory" to .csv
rename_files("my_directory", ".txt", ".csv")
