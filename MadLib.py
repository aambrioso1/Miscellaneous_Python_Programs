import random as rd  # A library for generating random numbers.
# import os  # A library for working with different operating systems we use it
# to read and write to our hard-drive.


# We create a function that generates a random number.  We use this to choose
# random words from our word list.
def rn():
    return rd.randint(0,7)

# Word lists for our MadLib
adjective = ['nice', 'mean', 'small', 'red', 'fluffy', 'scrappy', 'delicious', 'rotten']
noun = ['boy', 'girl', 'man', 'woman', 'dog', 'cat', 'octopus', 'fish']
pluralnoun = ['boys', 'girls', 'men', 'women', 'dogs', 'cats', 'octopuses', 'fish']
name =['Alex', 'Joseph', 'Erika', 'Sonya', 'Troy', 'Anthony', 'Steve', 'Ralph']

# We use an f-string to set up or MadLib with the positions where words from our
# list are used marked with {}.   Note how each line begins witn f".
MadLib = (
f"              Hangover Cures"
f"\n"
f"You\'re unsteady on your {noun[rn()]}, your breaking out in a cold {noun[rn()]}, and you have a splitting {noun[rn()]}-ache.   Yep, it\'s a hangover, and you need help:\n"
f"\n"
f"Cure \#1 - The Bloody {noun[rn()]} : There is no {adjective[rn()]} substitute.   The curative {pluralnoun[rn()]} in this {adjective[rn()]} drink are astonishing.\n"
f"\n"
f"Cure \#2 - The Coffee Cure: Many {pluralnoun[rn()]} swear that nothing equals {rn()} cups of black {noun[rn()]} to rid you of that {adjective[rn()]} headache.\n"
f"\n"
f"Cure \#3 - The Shower Cure:  This one works like a {noun[rn()]} for most people.   Stand under the {noun[rn()]} and alternate between hot and {adjective[rn()]} water.\n"
f"\n"
f"If these don't work, get on your cell {noun[rn()]} and call {name[rn()]}.  If she is a {adjective[rn()]} friend, she will cover your {noun[rn()]} at work.\n"
)

# We print our MadLib
print(MadLib)
