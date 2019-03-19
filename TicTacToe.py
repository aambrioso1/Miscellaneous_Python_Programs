# A Tic Tac Toe program by Alex Ambrioso (c) 2018

board = [['*','*','*'],['*','*','*'],['*','*','*']]
moves= ['TL', 'TC', 'TR', 'CL', 'CC', 'CR', 'BL', 'BC', 'BR']
values=('x','o')
turn='x'
move_key={'T':0, 'L':0, 'C':1,'B':2, 'R':2}

def printboard(board):
#Prints the current board
   for i in range(0,3):
      print("   %c%c%c" % (board[i][0],board[i][1],board[i][2]))

def instructions():
#Prints instructions for playing.
	print("Welcome to TicTacToe!")
	print("The first player will play x.")
	print("The second player will play o.")
	print("These are the allowable moves:\n")
	print("Type TL for the top left square.")
	print("Type TC for the top center square.")
	print("Type TR for the top right square.")
	print("Type CL for the center left square.")
	print("Type CC for the center square.")
	print("Type CR for the center right.")
	print("Type BL for the bottom left.")
	print("Type BC for the bottom center.")
	print("Type BR for the bottom right.")
	print("Type QUIT to stop playing.")
	print("Here is the board:")
	printboard(board)

def Wins(player, M):
#Checks to see if player has three in a row on board M.
	if player =='x':
		check ='o'
	else:
	 	check ='x'
	w=[]
	T_M=[[row[i] for row in M] for i in range(3)]
	#T_M is the transpose of M
	D1=[M[0][0],M[1][1],M[2][2]]
	#Downward diagonal elements of M
	D2=[M[2][0],M[1][1],M[0][2]]
	#Upward diagonal elements of M
	w.append((check not in D1) and ('*' not in D1))
	w.append((check not in D2) and ('*' not in D2))
	w.append((check not in M[0]) and ('*' not in M[0]))
	w.append((check not in M[1]) and ('*' not in M[1]))
	w.append((check not in M[2]) and ('*' not in M[2]))
	w.append((check not in T_M[0]) and ('*' not in T_M[0]))
	w.append((check not in T_M[1]) and ('*' not in T_M[1]))
	w.append((check not in T_M[2]) and ('*' not in T_M[2]))
	value = True in w
	return value

instructions()
while True:
	move=''
	while move not in moves or board[x][y] in values:
		print("%c moves" % (turn))
		move=input("Which square?\n")
		if move=='QUIT':
			break
		if len(move)>=2:
			x=move_key.get(move[0])
			y=move_key.get(move[1])
	if move=='QUIT':
		break
	board[x][y]=turn
	printboard(board)
	if Wins(turn, board):
		print("%c wins!" % (turn))
		break
	if turn=='x':
		turn='o'
	else:
		turn='x'

print("\nThanks for playing!!!")

