#Generates a list of m characters from the Characters list.
#The variable m controls the number of characters that will be generated.
#By setting the m to 3 the progams simulates one pull of a slot machine arm.
#myList is a list m random numbers between 1 and the length of the Characters list.
#PullList is a list of the characters in the Characters list that are in the positions indicated by myList
Characters=["~","!","@","#","$","%","&","*"]
import random
m=3
n=len(Characters)
myList=[random.randint(0,n-1) for i in range(m)]
PullList=[Characters[myList[i]] for i in range(m)]

print(PullList)
