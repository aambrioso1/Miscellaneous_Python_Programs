import os
#import Letter_Count a function that counts the different characters in a string.
from typing import TextIO

from Letter_Count import Count

#Access the name of the current working directory and its contents
path = os.getcwd()
print('The current working directory and its contents are: ', path,os.listdir(path))

#We create the pathname for the file containing the code for Letter_Code
path2 = str(path)+'\\Letter_Count.py'
print('\nThe path for the file Letter_Count.py is:', path2)

file = open(path2)
text = file.read()

print('\nThe text of Letter_Count.py is:\n\n', text)
textlist = Count(text)
print(textlist)

#This loop prints out the count for each character.
for i in range(len(textlist[0])):
    print('The number of %s\'s is %i' % (textlist[0][i],textlist[1][i]))
with open('tmp.txt', 'w') as handle:
    handle.writelines(['This is a test to see if I can write to the hard drive.\n', 'Let\'s see if it works!'])

path3 = str(path) + '\\tmp.txt'

file2 = open(path3)
text2 = file2.read()
print(text2)


file2.close()
file.close()
