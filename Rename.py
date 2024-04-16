import os


def bulk_rename(directory, new_names):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print("Error: Directory not found.")
        return

    # List all files in the directory
    files = os.listdir(directory)

    # Ensure there are the same number of files and new names
    if len(files) != len(new_names):
        print("Error: Number of files does not match number of new names.")
        return

    # Rename each file
    for old_name, new_name in zip(files, new_names):
        # Construct full file paths
        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(directory, new_name)

        # Rename the file
        try:
            os.rename(old_path, new_path)
            print(f"Renamed '{old_name}' to '{new_name}'.")
        except Exception as e:
            print(f"Error renaming '{old_name}': {str(e)}")

def get_current_working_directory():
    cwd = os.getcwd()
    return cwd


if __name__ == "__main__":
    directory = get_current_working_directory()  # Replace with your directory path

    new_file_name = []
    # Replace with your list of new names
    bulk_rename(directory, new_file_name)
