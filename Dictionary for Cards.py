#The dictionary Cards serves as a data structure for a deck of cards.  A tuple (denomination, suit) serves as the key.
#This structure attempts to capture the way a person thinks of the cards.

Dens=['Ace','Two','Three','Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
Suits=['Spades', 'Hearts', 'Clubs', 'Diamonds']
Colors=['Black', 'Red']
Vals=[[1,11]]+[i for i in range(2,11)]+[10,10,10]

for i in range(52):
	print(Dens[i%13],Suits[i%4],Vals[i%13],Colors[i%2])

Cards={(Dens[i%13],Suits[i%4]):{'Value':Vals[i%13],'Suit':Suits[i%4],'Color':Colors[i%2]} for i in range(52)}

#Print the value of the ace of spades.
print('\n')
print(Cards[('Ace','Spades')]['Value'], '\n')

#Print the value color of the two of hearts.
print(Cards[('Two', 'Hearts')]['Color'])
