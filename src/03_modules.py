"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print("This is the name of the program:", sys.argv[0])
# This prints the file name


# Print out the OS platform you're using:
print("The platform I am using is:", sys.platform)
# This prints win32 for me as it is a windows pc



# Print out the version of Python you're using:
print('The python version I have is:', sys.version)
# This prints 3.8.5 as that is the pythong version installed


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
pid = os.getpid()
print(pid)
# This prints the current process running


# Print the current working directory (cwd):
path = os.getcwd()
print(path)
# This will print the current file location or path


# Print out your machine's login name
name = os.getlogin()
print(name)
# On this pc it will print irish as that is the username of this pc
