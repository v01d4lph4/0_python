# 14. file handling

# file handling is an important part of any web application.
# python has several functions for creating, reading, updating, and deleting files

# ⚙️ syntax   : open(filename, mode)
# filename    : path to file (text/binary)
# mode        : represents the purpose of the opening file, supported modes are:
#              - r: open an existing file for a read operation.
#              - w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
#              - a:  open an existing file for append operation. It won’t override existing data.
#              - r+:  To read and write data into the file. The previous data in the file will be overridden.
#              - w+: To write and read data. It will override existing data.
#              - a+: To append and read data from the file. It won’t override existing data.
# returns a iterable file object

# to read a file 
file = open("v01d.txt")                             # default mode = "rt" ~ read / text
print(file.read())
file.close()                                        # close() command terminate the resources in use 

# to create/write a file 
file = open("v01d.txt", "wt")                       # "w" ~ write mode
file.write("0. h3ll0, w0r1d!")
file.write("1. 1337 h4xx0r")
file.close()

# to append a line to file
file = open("v01d.txt", "a")                        # "a" ~ append mode (t is by default)
file.write("2. d3adb33f")                           # this will append line 3 at end of file
file.close()

# 💡 protip: more pythonic way to open a file
with open("v01d.txt", "r") as file:                 # with() ensure the close() is called automatically
    data = file.read()


# 🎁 bonus: to delete a file, if it exists
import os

if os.path.exists("v01d.txt"):
  os.remove("v01d.txt") 
else:
  print("The file does not exist")
