import os

# 1
# os.mkdir()
# This function takes the path of the new directory you want to create and creates it for you. It will give you an error if the path you enter exists
# os.mkdir("images")

# 2
# os.listdir() 
# This function returns all the files and directories in the input path
print(os.listdir())

# 3
# os.remove()
# To remove a file from a directory, you can use the remove() function to perform this operation. To do this, you need to provide the path of the file you want to delete as input

# os.remove("image")

# 4
# os.getcwd()
# This function returns the address of where you are now
print(os.getcwd())