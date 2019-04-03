#Input a string, create a list of the different characters in the string, then count how many of each character

def CountChar(chr,list):
#This function inputs an item and a list and counts how many of item are in the list.
        count=0
        for i in list:
                if i==chr:
                        count+=1
        return count

def RemoveChar(char, list):
#This function removes the item, char, from the list.
 while(char in list):
        list.remove(char)
 return(list)

#The lists used in the program are initialized as empty lists.
countlist=[]
list=[]
templist=[]
charlist=[]


#This loop creates two lists of all the characters in the user's text.
def Count(text):
        for i in range(len(text)):
                list.append(text[i])
                templist.append(text[i])

#This loops removes all the repeated characters in templist and creates a list of how many of each character were in the user's text.
        charlist=[]
        while(len(templist)>0):
                countlist.append(CountChar(templist[0], list))
                k=templist[0]
                RemoveChar(k,templist)
                charlist+=k
        return [charlist,countlist]

#print(Count('Alexander Ambrioso'))
