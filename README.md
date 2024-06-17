# Easy File Mover GUI App
A Python-based GUI application designed to help you move and organize files from a source directory to a destination directory. It also maintains a history of moved files for easy tracking.

## Features

- Move files from a specified source directory to a destination directory.
- Maintain a history of moved files in a text file.
- User-friendly GUI for easy directory selection.
- Default directories and history file locations are pre-configured for convenience.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages: `tkinter`, `shutil`, `pathlib`, `datetime`

### Installation

1. **Download the script:**

   Download the `script.pyw` file from the repository.

2. **Run the script:**

   Double-click the `script.pyw` file to launch the GUI application, or run `python script.pyw` in your terminal.
   Better to just create a shortcut on your desktop and double-click to launch it.

### Default Configuration
By default it works for Windows, you'll need to adjust the default paths to match the directory structure of these operating systems (e.g., /home/username/Downloads for Linux or /Users/username/Downloads for macOS).

Change the default directories in the script file accordingly:
```python
DEFAULT_HISTORY_FILE = r"C:\Users\saif\OneDrive\Desktop\moved-file-history.txt"
DEFAULT_SOURCE_DIR = r"C:\Users\saif\Downloads"
DEFAULT_DEST_DIR = r"D:\downloaded_files"
```

### Usage

1. **Select Source Directory:**

   Click the "Browse" button next to "Source Directory" to select the directory from which files will be moved.

2. **Select Destination Directory:**

   Click the "Browse" button next to "Destination Directory" to select the directory where files will be moved.

3. **Use Default Directories:**

   Click the "Default" button to use the pre-configured default directories:
   - Source: `C:\Users\saif\Downloads`
   - Destination: `D:\downloaded_files`

4. **Start Moving Files:**

   Click the "Start Moving Files" button to move files from the source directory to the destination directory. The move history will be recorded in the specified history file.



