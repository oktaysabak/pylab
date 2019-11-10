import os

path_joiner = os.path.join('usr','bin') # join your list via your OS separator 
print('joined path is: {}'.format(path_joiner)) # joined path is: usr/bin
current_directory = os.getcwd() # get current directory
print('current directory is: {}'.format(current_directory)) # current directory is: /home/okito/paylab
print('changing directory to humblebumble...')
try:
    os.chdir('humblebumble') # change your directory to the parameter
    current_directory = os.getcwd()
    print('we are in {} now'.format(current_directory)) # we are in /home/okito/paylab/humblebumble now
except:
    print('we cant find humblebumble directory')
absolute_path = os.path.abspath('.') # get absolute path of parameter
print('our absolute path is: %s' %absolute_path) # our absolute path is: /home/okito/paylab/humblebumble
base_name = os.path.basename('./osmodule.py') # get basename of the parameter 
print('base name "./osmodule.py" is: {}'.format(base_name)) # base name "./osmodule.py" is: osmodule.py
dir_name = os.path.dirname('./osmodule.py') # directory name of parameter
print('dir name of "./osmodule.py" is: {}'.format(dir_name)) # dir name of "./osmodule.py" is: .
splitted_current_path = current_directory.split(os.path.sep) 
# split current directory with OS separator. result ['', 'home', 'okito', 'paylab', 'humblebumble']
print('split current directory with OS separator. result {}'.format(splitted_current_path))
list_of_current_directory = os.listdir(current_directory) # list inside of given parameter
print('files in  {}'.format(list_of_current_directory))
# directories in  ['random_team.py', '__init__.py', 'regexwork.py', 'app2.py', 'dict_ex.py', 'app.py', 'osmodule.py', 'app3.py']
size_of_file = os.path.getsize('osmodule.py') # get size of file as bytes
print('size of osmodule.py is {} bytes'.format(size_of_file))
total_size_of_python_files = 0
for fl in list_of_current_directory:
    if 'py' in fl:
        total_size_of_python_files += os.path.getsize(fl)
print('total size of python files in current directory is {} bytes'.format(total_size_of_python_files))
os.path.exists('humblebumble') # check if exists
os.path.isdir('humblebumble') # check if parameter is a directory
os.path.isfile('osmodule.py') # check if parameter is a file