import os

# Access the name of the current working directory and its contents
path = os.getcwd()
print('The current working directory and its contents are: ', path, os.listdir(path))

