import os
from shutil import move
import shutil

files = []
def find_files(directory):
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)
        if os.path.isfile(full_path) and not file.startswith(".") and not file.__eq__(__file__):
            files.append(full_path)

def move_files(directory, extension):
    for file in files:
        if(file.endswith(extension)):
            try:
                move(file, directory)
                return ""
            except shutil.Error as e:
                return os.path.basename(file)

def delete_files(extension):
    for file in files:
        if(file.endswith(extension)):
            os.remove(file)