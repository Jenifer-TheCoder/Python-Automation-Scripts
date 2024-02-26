import os
import shutil
from datetime import datetime, timedelta

def cleanup_folders(folder_paths, max_age_days):
    # Get the current date and time
    current_datetime = datetime.now()

    for folder_path in folder_paths:
        # Check if the folder exists
        if os.path.exists(folder_path):
            print(f"Cleaning up {folder_path}")

            # Iterate over files in the folder
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)

                # Get the file's last modification time
                last_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))

                # Calculate the age of the file in days
                file_age_days = (current_datetime - last_modified_time).days

                # Check if the file is older than the specified max age
                if file_age_days > max_age_days:
                    if os.path.isfile(file_path):
                        # Remove the file
                        os.remove(file_path)
                        print(f"Removed file: {file_name}")
                    elif os.path.isdir(file_path):
                        # Remove the directory and its contents
                        shutil.rmtree(file_path)
                        print(f"Removed directory: {file_name}")

# Define the folders to clean up and the maximum age of files to keep (in days)
folders_to_cleanup = ['/path/to/temp', '/path/to/downloads']
max_file_age_days = 7

# Perform the cleanup
cleanup_folders(folders_to_cleanup, max_file_age_days)
