import os

#Access the name of the current working directory and its contents
path = os.getcwd()
print('The current working directory and its contents are: ', path,os.listdir(path))

name=input('What is your name?\n')

with open('names.txt', 'a') as f1:
        f1.write(name+'\n')

with open('times.txt', 'a') as f2:
        f2.write(str(10)+'\n')

path1 = str(path) + '\\names.txt'
path2 = str(path) + '\\times.txt'

with open(path1) as f1:
    lines1 = [x.rstrip() for x in f1]

with open(path2) as f2:
    lines2 = [x.rstrip() for x in f2]

print(lines1,lines2)



