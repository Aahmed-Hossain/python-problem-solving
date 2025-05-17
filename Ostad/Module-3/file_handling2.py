import os
import pathlib

if os.path.exists('file.txt'):
    print('file exist')
else:
    print('file not found')

file_path = pathlib.Path('file.txt')
if file_path.exists():
    print('file exist')
print(os.path.abspath('file.txt'))
print(os.path.getsize('file.txt'))
