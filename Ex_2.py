'''
I was having a lot of issues with file paths and Pycharm using a working directory that was different to the
directory I was working in.
All the following commands are also script specific.
'''

# Saving files to a specific folder (without changing the working directory):

import os.path

save_path = 'C:/example/'

name_of_file = input("What is the name of the file: ")

completeName = os.path.join(save_path, name_of_file+".txt")

file1 = open(completeName, "w")

toFile = input("Write what you want into the field")

file1.write(toFile)

file1.close()

'''
You can also check if a folder exists and, if it doesn't, create a new one using Python:
'''

if not os.path.exists("data"):
    os.mkdir("data")