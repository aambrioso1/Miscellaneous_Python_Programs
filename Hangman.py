import random

wordlist=['zebra', 'money', 'python', 'science', 'data', 'games']
guessedset=set()
guessedit=False

def inputaletter():
    check=False
    while(check==False):
        print('\nLetters guessed so far: ', list(guessedset))
        letter=input('Please input a letter: \n')
        check=len(letter)==1 and letter.isalpha() and True#check if used
    return(letter)


def pickaword(list):
    num = random.randint(0,len(wordlist)-1)
    return list[num]

def outputlist(guessedlist, letterlist):
    templist=[]
    for i in letterlist:
        if i in guessedlist:
             templist.append(i)
        else: templist.append('__ ')
    return templist

def printbars():
    print('**********************************************')

word=pickaword(wordlist)
letterlist=[word[i] for i in range(len(word))]
out=outputlist([], letterlist)

printbars()
print('Try to guess the letters in the %i-letter word.' % (len(word)))
print('         ',''.join(out))
printbars()

while(guessedit==False):
    newletter=inputaletter()
    guessedset.add(newletter)
    out=outputlist(guessedset,letterlist)
    printbars()
    print('         ',''.join(out))
    printbars()
    if out==letterlist:
        guessedit=True

print('\nGreat job. You guessed it!', word)

