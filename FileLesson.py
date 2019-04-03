#This is a lesson on reading and writing to files in Python.
# we inport the operating system library. "This module provides a portable way of using operating system dependent functionality."
# This is the description found in the Python documentation at https://docs.python.org/3/library/os.html

#First we create a text file named tmp.txt.This file should contain a couple of sentences.
import os

#We access the name of the current working directory (cwd) and its contents
path = os.getcwd()
print('The current working directory:', path)
print('\nThe current working its contents is:\n\n', os.listdir(path))


#We import Letter_Count a function that counts the different characters in a string.
from Letter_Count import Count

# We create a path for a file named tmp.txt.
filename='tmp.txt'
path2 = str(path)+ '/' + filename
print('\nThe path of ' + filename + ' is:', path2)

#file = open(path2)
file = open('tmp.txt')
text = file.read()

print('\nThe text of ' + filename + ' is:\n\n', text)
countlist = Count(text)
print('\nThe result of our count is:\n\n', countlist)
