# week8_file_organizer.py

import os
import shutil

def organize_files(folder_path):
    """Organize files in folder by their extension."""
    if not os.path.exists(folder_path):
        print("❌ Folder not found.")
        return
    
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            ext = file.split(".")[-1].lower()
            ext_folder = os.path.join(folder_path, ext)
            os.makedirs(ext_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(ext_folder, file))
    print("✅ Files organized successfully!")

def main():
    folder_path = input("Enter folder path to organize: ")
    organize_files(folder_path)

if __name__ == "__main__":
    main()
