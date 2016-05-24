# Remove file or folder recursively
import os
import shutil
import sys, getopt

def rmfile(dir_path, filename):
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        if name == filename:
            if os.path.isfile(full_path):
                os.remove(full_path)
            elif removeDirectory:
                shutil.rmtree(full_path)
        elif os.path.isdir(full_path):
            rmfile(full_path, filename)

def usage():
    print('rmfile.py usage:')
    print('-r file to remove')
    print('-d remove matched directory')

dir_path = ""
filename = ""
removeDirectory = False

opts, args = getopt.getopt(sys.argv[1:], "r:d")

if len(args) == 0:
    usage()
    sys.exit()
dir_path = args[0]

for op, value in opts:
    if op == "-r":
        filename = value
    elif op == '-d':
        removeDirectory = True
    else:
        usage()
        sys.exit()

rmfile(dir_path, filename)

