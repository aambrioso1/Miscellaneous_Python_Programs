#This is a lesson on reading and writing to files in Python.
# we import the operating system library. "This module provides a portable way of using operating system dependent functionality."
# This is the description found in the Python documentation at https://docs.python.org/3/library/os.html

#First we create a text file named tmp.txt.This file should contain a couple of sentences.
import os

#We access the name of the current working directory (cwd) and its contents
path = os.getcwd()
print('The current working directory:', path)
print('\nThe current working its contents is:\n', os.listdir(path))


#We import Letter_Count a function that counts the different characters in a string.
from Letter_Count import Count

# We create a path for a file named tmp.txt.
filename='tmp.txt'
path2 = str(path)+ '/' + filename
print('\nThe path of ' + filename + ' is:', path2)

#file = open(path2)
file = open('tmp.txt')
text = file.read()
file.close()

print('\nThe text of ' + filename + ' is:\n', text)
countlist = Count(text)
print('\nThe result of our count is:\n', countlist)

#This loop prints out the count for each character.
print('\nThe file tmp.txt has the following characters:')
for i in range(len(countlist[0])):
    print('The number of %s\'s is %i' % (countlist[0][i],countlist[1][i]))

#This will write the results for count to a file called count.txt
with open('count.txt', 'w') as handle:
    handle.writelines(str(countlist[0])+'\n'+ str(countlist[1]))
