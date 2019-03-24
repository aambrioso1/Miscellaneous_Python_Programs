import random
high=100
go=True
number = random.randint(1,high)

while go==True:
	guess=input("Try to guess a number between 1 and 100\n")
	guess=int(guess)
	if guess>number:
		print("Too high!")
	elif guess<number:
		print("Too low!")
	elif guess==number:
		print("Correct!")
		again=input("Play again? (Y or N)\n")
		if again=="n" or again=="N":
			go=False
		number = random.randint(1,high)
print("Thanks for playing")
