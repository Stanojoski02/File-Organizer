# File-Organizer
The File Organizer is a script designed to help users organize files in a directory by categorizing them into folders based on their file types. This can be particularly useful for keeping your workspace tidy and ensuring that files are easy to find.
# File-Organizer

The File Organizer is a script designed to help users organize files in a directory by categorizing them into folders based on their file types. This can be particularly useful for keeping your workspace tidy and ensuring that files are easy to find.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [Contributors](#contributors)
- [License](#license)

## Features

- Organizes files into predefined categories (e.g., Documents, Spreadsheets, Images, Audio).
- Supports a wide range of file types.
- Allows for organizing all files or specific file types.
- Creates necessary directories if they do not exist.

## Installation

1. Clone the repository or download the script file.
2. Ensure you have Python installed (version 3.6 or higher).

## Usage

To use the File Organizer, run the script with the appropriate arguments.

### Command-Line Arguments

- `--type`: (Optional) Specify the file type to organize (e.g., `pdf`). If not specified, all file types will be organized.
- `--path`: (Optional) Specify the target directory for organizing files. If not specified, the current working directory will be used.
### Example

```bash
python file_organizer.py --type pdf --path /path/to/directory
