import os
#import Letter_Count
from Letter_Count import Count

path=os.getcwd()
print('The current working directory and its contents are: ', path,os.listdir(path))

path2=str(path)+'\\Letter_Count.py'
print('\nThe path for the file Letter_Count.py is:', path2)



file = open(path2)
text=file.read()

print('\nThe text of Letter_Count.py is:\n\n', text)
textlist=Count(text)
print(textlist)

#This loop prints out the count for each character.
for i in range(len(textlist[0])):
    print('The number of %s\'s is %i' % (textlist[0][i],textlist[1][i]))


file.close()

