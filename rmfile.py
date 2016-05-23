# remove file or folder recursively
import os
import shutil

def rmfile(dir_path, filename, recursively):
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        if name == filename:
            if os.path.isdir(full_path):
                shutil.rmtree(full_path)
            else:
                os.remove(full_path)
        elif os.path.isdir(full_path):
            rmfile(full_path, filename, recursively)

rmfile('D:\\a', 'rm', True)
