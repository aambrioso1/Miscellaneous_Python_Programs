# This is a lesson on reading and writing to files in Python.  We will also learn how to import function defined in another program file.

# First we create a text file named tmp.txt.  This file should contain a couple of sentences at least.   Use Notepad to create it.
# It should be stored on in the current working directory (cwd) for your Python compiler.

# We import the operating system library. "This module provides a portable way of using operating system dependent functionality."
# This is the description found in the Python documentation at https://docs.python.org/3/library/os.html
import os

# We access the name of the current working directory and its contents.
path = os.getcwd()
print('The current working directory:', path)
print('\nThe current working its contents is:\n', os.listdir(path))

# We import Letter_Count a function that counts the different characters in a string.
# The is a program I wrote that counts characters in text.
# It takes a single string and returns a list of two lists.
# The first list is a list of all the different characters in the text.
# The second one is a list of the corresponding frequencies of each letter in the first list.
from Letter_Count import Count

# We create a path for a file named tmp.txt.
filename='tmp.txt'
path2 = str(path)+ '/' + filename
print('\nThe path of ' + filename + ' is:', path2)

# We open the file tmp.txt and save its contents to the variable text.  Then we close the file.
file = open('tmp.txt')
text = file.read()
file.close()

#  We print out the text in tmp.txt and the result of Count(text).
print('\nThe text of ' + filename + ' is:\n', text)
countlist = Count(text)
print('\nThe result of our count is:\n', countlist)

# This loop prints out the count for each character.
print('\nThe file tmp.txt has the following characters:')
for i in range(len(countlist[0])):
    print('The number of %s\'s is %i' % (countlist[0][i],countlist[1][i]))

# This will write the results of Count(text) to a file called count.txt
with open('count.txt', 'w') as handle:
    handle.writelines(str(countlist[0])+'\n'+ str(countlist[1]))
