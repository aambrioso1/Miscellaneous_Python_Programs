#The classic game of rock-paper-scissors by Alex Ambrioso @2019

import random #This imports the library with methods for generating random numbers.

plays = ['p','r','s']  #This is a list of the valid strings that a player can input: paper (p), rock(r), or scissors(s).
checked = False #This variable is used to decide if the player input a valid play.
go = True   #This variable is used to decide if the player wants to play again.  If go is true the player wants to play again.
            #It go is false then the player does not want to play again.

#This function generates one of the three possible plays at random.
#This is the function that uses the random library.
#Note that the method we use is randint(a, b) which generates a random number between a and b inclusive.
def playgen():
        rand = random.randint(0,2)
        if rand == 0: return 'r'
        elif rand == 1: return 'p'
        elif rand == 2: return 's'

print('Follow the instructions to play the classic game of rock-paper-scissor against the computer\n\n')


while(go):  #This while loop continues until the palyer does not want to play anymore.
        while not checked: #This while loop continues until the player inputs a valid play.
                play = input('\nWould you like to play rock(r), paper(p), or scissors(s)?\n\n')
                if play in plays:
                        checked = True
                        print('\nYou played %s.\n' % play) #Once the player makes a valid play we print it out.
                else: print('\n%s is not a valid play.\n' % play)  #If the player does not input a valid play, we let the player know and loop back.

        # We generate a play for the computer using the function, playgen(), we defined earlier.
        #Note that playgen() takes no argument and it returns a play.  We use the variable cplay to store the computer's play.

        cplay = playgen()

        # We print out the computers play.
        print('The computer played %s.\n' % cplay)
        print('*************************************************\n')

        #Now we compare the player's play and the computer's play and decide what the result should be.
        if play == cplay: print('It\'s a tie\n')
        elif play == 'r' and cplay == 's':
                print('Rock smashes scissors so you win!\n')
        elif play == 'r' and cplay == 'p':
                print('Paper covers rock so the computer wins!\n')
        elif play == 's' and cplay == 'r':
                print('Rock smashes scissors so the computer wins!\n')
        elif play == 'p' and cplay == 'r':
                print('Paper covers rock so you win!\n')
        elif play == 's' and cplay == 'p':
                print('Scissors cut paper so you win!\n')
        elif play == 'p' and cplay == 's':
                print('Scissors cut paper so the computer wins!\n')
        print('*************************************************\n')

        #Now we check if the player wants to play again.
        again = input('Would you like to play again? Yes (Y) or No (N).\n\n\n')
        if again in ['N', 'No', 'n', 'no']:
                go = False
        #If we get here then the player want to play again.  So we set checked back to false
        #so that when we go back to the top we check again if player is making a valid play.
        checked = False

#If we get here the player has decided to stop playing.
print('\n\nThanks for playing!\n')
