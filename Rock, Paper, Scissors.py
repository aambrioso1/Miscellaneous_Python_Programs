#The classic game of rock-paper-scissors by Alex Ambrioso @2019

import random

plays=['p','r','s']
checked=False
go=True

def playgen():
        rand=random.randint(0,2)
        if rand==0: return 'r'
        elif rand==1: return 'p'
        elif rand==2: return 's'

print('Follow the instructions to play the classic game of rock-paper-scissor against the computer\n\n')


while(go):
        while(not checked):
                play=input('\nWould you like to play rock(r), paper(p), or scissors(s)?\n\n')
                if play in plays:
                        checked=True
                        print('\nYou played %s.\n' % play)
                else: print('\n%s is not a valid play.\n' % play)

        cplay=playgen()

        print('The computer played %s.\n' % cplay)

        if play==cplay: print('It\'s a tie\n')
        elif (play=='r' and cplay=='s'):
                print('Rock smashes scissors so you win!\n')
        elif play=='r' and cplay=='p':
                print('Paper covers rock so the computer wins!\n')
        elif play=='s' and cplay=='r':
                print('Rock smashes scissors so the computer wins!\n')
        elif play=='p' and cplay=='r':
                print('Paper covers rock so you win!\n')
        elif play=='s' and cplay=='p':
                print('Scissors cut paper so you win!\n')
        elif play=='p' and cplay=='s':
                print('Scissors cut paper so the computer wins!\n')

        again=input('Would you like to play again? Yes (Y) or No (N).\n\n\n')
        checked=False

        if again in ['N','No','n','no']:
                go = False
print('\n\nThanks for playing!\n')
