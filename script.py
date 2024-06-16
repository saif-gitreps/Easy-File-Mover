import os
import shutil
from pathlib import Path

def organize_files(source_dir, destination_dir):
    Path(destination_dir).mkdir(parents=True, exist_ok=True)
    
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)

        if os.path.isfile(source_path):
            try:
                dest_path = os.path.join(destination_dir, item)
                shutil.move(source_path, dest_path)
                print(f"Moved {source_path} to {dest_path}")
            except Exception as e:
                print(f"Error moving {source_path} to {dest_path}: {e}")


if __name__ == "__main__":
    #example destination and source directories
    source_directory = r"C:\Users\saif\Downloads"
    destination_directory = r"D:\downloaded_files"

    organize_files(source_directory, destination_directory)
 