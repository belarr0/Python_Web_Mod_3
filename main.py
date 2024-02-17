import os
import shutil
import threading

def sort_files_by_extension(source_folder):
    files_by_extension = {}
    files = os.listdir(source_folder)


    for file in files:
        _, extension = os.path.splitext(file)

        file_path = os.path.join(source_folder, file)

        if os.path.isfile(file_path):
            if extension not in files_by_extension:
                files_by_extension[extension] = []
            files_by_extension[extension].append(file_path)


    for extension, files in files_by_extension.items():
        destination_folder = os.path.join(source_folder, extension)
        os.makedirs(destination_folder, exist_ok=True)

        for file_path in files:
            threading.Thread(target=shutil.move, args=(file_path, destination_folder)).start()


def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    source_folder = os.path.join(current_directory, "Hlam")

    sort_files_by_extension(source_folder)

if __name__ == "__main__":
    main()
