"""
The shutil module provides functions for copying files, as well as entire folders.
"""
import shutil, os
from pathlib import Path
import time
try:
    file_name = input('Write file name which will copy to HOME: ')
    if shutil.copy(file_name, Path.home()): # copy file to destination
        print('file copied')
        print('list of your HOME directory')
        print(os.listdir(Path.home())) # Path.home() for get our home directory
        time.sleep(2)
        print('deleting created file from home')
        os.remove(file_name)
except FileNotFoundError:
    print('cannot find the file')

# shutil.copytree('source_directory', 'destination_directory') copying directories

try:
    print('creating temporary file')
    file_name = input('Write file name which will move to HOME: ')
    with open(file_name, 'w') as f:
        f.write('this is empty file')
        print('{} created'.format(file_name))
        time.sleep(2)
    
    try:
        if file_name not in os.listdir(Path.home()): # copy file to destination
            shutil.move(file_name, Path.home())
            print('{} moved to {}'.format(file_name, Path.home()))
            print('list of your HOME directory')
            print(os.listdir(Path.home())) # Path.home() for get our home directory
            print('deleting moved {} from {}'.format(file_name, Path.cwd()))
            time.sleep(2)
            #os.remove(file_name) # remove file from current page
            print('deleting moved {} from {}'.format(file_name, Path.home()))
            home = Path.home()
            os.unlink(str(home) + '/' + file_name) # unlink path
        else:
            print('{} already exists'.format(file_name))
    except shutil.Error:
        print('shutil has an error')

except FileNotFoundError:
    print('File deleted successfully')

"""
Also:
•Calling os.unlink(path) will delete the file at path .
•Calling os.rmdir(path) will delete the folder at path . This folder must be
empty of any files or folders.
•Calling shutil.rmtree(path) will remove the folder at path , and all files
and folders it contains will also be deleted.
"""