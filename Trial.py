import numpy as np
import os

# Access the name of the current working directory and its contents
path = os.getcwd()
print('The current working directory and its contents are: ', path, os.listdir(path))


arr = np.arange(10)
print('array: ', arr)
filename = 'some array'
path2 = str(path) + '/' + filename

np.save(path2, arr)

# Access the name of the current working directory and its contents
path = os.getcwd()
print('The current working directory and its contents are: ', path, os.listdir(path))
