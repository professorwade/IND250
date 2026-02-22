import os
from pathlib import Path
import platform
import sys

# get current working directory as a string
print(os.getcwd())

# list files in a directory
files = os.listdir('.')
for f in files:
    print(f)

# get operating system
print(os.name)

# find out if a file exists
print(os.path.exists('file_handling.py'))

# create a file
Path('new_file.txt').touch()
# you can also delete, rename, move, etc., but be careful

# walk a directory
for root, dirs, files in os.walk("."):
    print(f"Current Directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")
    print("-" * 20)

print("OS Name (platform.system()):", platform.system())
print("OS Release:", platform.release())
print("OS Version:", platform.version())
print("Machine Architecture:", platform.machine())
print("Full Platform Info:", platform.platform())

print("System Platform Identifier:", sys.platform)

if sys.platform.startswith('win'):
    print("Running on Windows")
elif sys.platform.startswith('linux'):
    print("Running on Linux")
elif sys.platform.startswith('darwin'):
    print("Running on macOS")

