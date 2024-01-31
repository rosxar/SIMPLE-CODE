import os
import shutil

def move_files_to_main_folder(root_folder):
    # Loop through subfolders
    for foldername, subfolders, filenames in os.walk(root_folder):
        # Skip the root folder to avoid moving files from the main folder
        if foldername == root_folder:
            continue

        # Move each file to the main folder
        for filename in filenames:
            source_path = os.path.join(foldername, filename)
            destination_path = os.path.join(root_folder, filename)

            # Check if the file already exists in the main folder
            if not os.path.exists(destination_path):
                shutil.move(source_path, destination_path)
                print(f"Moved: {filename} from {foldername} to {root_folder}")
            else:
                print(f"File {filename} already exists in {root_folder}. Skipping.")

if __name__ == "__main__":
    # Ganti path_folder_utama dengan path folder utama Anda
    path_folder_utama = 'LOKASI\\FOLDER\UTAMA'
    move_files_to_main_folder(path_folder_utama)
