import os

#Access the name of the current working directory and its contents
path = os.getcwd()

texttime=input('Input a floating put number\n')
time = float(texttime)

path1 = str(path) + '\\times.txt'

with open('times.txt') as f1:
    oldtime = float(f1.read())

if time < oldtime:
    with open('times.txt', 'w') as f1:
        f1.write(str(time))


with open(path1) as f1:
    besttime =f1.read()

print(besttime)
