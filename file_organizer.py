import os
import shutil
import argparse

file_types = {
    'pdf': 'Documents',
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    'rtf': 'Documents',
    'odt': 'Documents',
    'xls': 'Spreadsheets',
    'xlsx': 'Spreadsheets',
    'csv': 'Spreadsheets',
    'ods': 'Spreadsheets',
    'ppt': 'Presentations',
    'pptx': 'Presentations',
    'odp': 'Presentations',
    'jpg': 'Images',
    'jpeg': 'Images',
    'png': 'Images',
    'gif': 'Images',
    'bmp': 'Images',
    'tiff': 'Images',
    'tif': 'Images',
    'svg': 'Images',
    'mp3': 'Audio',
    'wav': 'Audio',
    'aac': 'Audio',
    'flac': 'Audio'
}


def get_file_extension(filename):
    return filename.split('.')[-1].lower()


def organize_files(files, file_types, destination_dir, specific_type=None):
    for file in files:
        if os.path.isdir(file):
            continue
        file_extension = get_file_extension(file)
        if specific_type and file_extension != specific_type:
            continue
        if file_extension in file_types:
            dir_name = os.path.join(destination_dir, file_types[file_extension])
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            shutil.move(file, os.path.join(dir_name, file))


def parse_arguments():
    parser = argparse.ArgumentParser(description='Organize files in the specified directory.')
    parser.add_argument('--type',
                        help='Specify the file type to organize (e.g., pdf). If not specified, all file types will be organized.')
    parser.add_argument('--path', help='Specify the target directory for organizing files.')
    return parser.parse_args()


def main():
    args = parse_arguments()
    specific_type = args.type
    destination_dir = os.path.abspath(args.path) if args.path else os.getcwd()
    files = os.listdir(destination_dir)
    os.chdir(destination_dir)
    organize_files(files, file_types, destination_dir, specific_type)


if __name__ == '__main__':
    main()
