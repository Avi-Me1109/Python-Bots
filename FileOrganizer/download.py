import os
from shutil import move

files = []
def find_files(directory):
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)
        if os.path.isfile(full_path) and not file.startswith(".") and not file.__eq__(__file__):
            files.append(full_path)

def move_files(directory, extension):
    for file in files:
        if(file.endswith(extension)):
            move(file, directory)

def delete_files(extension):
    for file in files:
        if(file.endswith(extension)):
            os.remove(file)