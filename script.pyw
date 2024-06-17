import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

DEFAULT_HISTORY_FILE = r"C:\Users\saif\OneDrive\Desktop\moved-file-history.txt"
DEFAULT_SOURCE_DIR = r"C:\Users\saif\Downloads"
DEFAULT_DEST_DIR = r"D:\downloaded_files"

def move_files(source_dir, dest_dir):
    try:
        # Create the destination directory if it doesn't exist
        Path(dest_dir).mkdir(parents=True, exist_ok=True)

        history = []
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            dest_path = os.path.join(dest_dir, item)
            
            # Recording the move history
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history.append(f"{timestamp}: Moved '{str(item)}' from '{source_path}' to '{dest_path}'")
            
            shutil.move(source_path, dest_path)
            print(f"Moved {source_path} to {dest_path}")

        # documenting the move history in txt file
        with open(DEFAULT_HISTORY_FILE, 'a') as file:
            for entry in history:
                file.write(entry + '\n')
                file.write('\n')
                
        messagebox.showinfo("Success", "Items moved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error moving items: {e}")

def select_source_dir():
    source_dir = filedialog.askdirectory()
    if source_dir:
        source_entry.delete(0, tk.END)
        source_entry.insert(0, source_dir)

def select_dest_dir():
    dest_dir = filedialog.askdirectory()
    if dest_dir:
        dest_entry.delete(0, tk.END)
        dest_entry.insert(0, dest_dir)

def start_moving():
    source_dir = source_entry.get()
    dest_dir = dest_entry.get()
    if not source_dir or not dest_dir:
        messagebox.showwarning("Warning", "Please select both source and destination directories.")
    else:
        move_files(source_dir, dest_dir)
        
def move_default():
    source_entry.delete(0, tk.END)
    source_entry.insert(0, DEFAULT_SOURCE_DIR)
    
    dest_entry.delete(0, tk.END)
    dest_entry.insert(0, DEFAULT_DEST_DIR)

root = tk.Tk()
root.title("File Mover Organizer")

source_label = tk.Label(root, text="Source Directory:")
source_label.grid(row=0, column=0, padx=10, pady=10)

source_entry = tk.Entry(root, width=50)
source_entry.grid(row=0, column=1, padx=10, pady=10)

source_button = tk.Button(root, text="Browse", command=select_source_dir)
source_button.grid(row=0, column=2, padx=10, pady=10)

dest_label = tk.Label(root, text="Destination Directory:")
dest_label.grid(row=1, column=0, padx=10, pady=10)

dest_entry = tk.Entry(root, width=50)
dest_entry.grid(row=1, column=1, padx=10, pady=10)

dest_button = tk.Button(root, text="Browse", command=select_dest_dir)
dest_button.grid(row=1, column=2, padx=10, pady=10)

dest_button = tk.Button(root, text="Default", command=move_default)
dest_button.grid(row=2, column=2, padx=10, pady=10)

start_button = tk.Button(root, text="Start Moving Files", command=start_moving)
start_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
