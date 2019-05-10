# We will demonstrate the Law of Large Numbers by simulating die rolls.   As the number of die rolls increases the relative frequency of each number should approach the theoretical probability of 1/6.

# We will use the function randint from the random library.  The function is described below.

from random import randint

# The function randint(1,6) simulates a die roll by returning a random integer between 1 and 6.

# Roll a die once.
print('We rolled a die once and roll a %i.\n' % (randint(1, 6)))


# This function creates a list of n die rolls.
def rolldie(num):
    roll_list = []
    for k in range(num):
        roll_list.append(randint(1, 6))
    return roll_list


# The variable n is the number of times we are rolling the die.  Try running the program with different values of n to demonstrate the LOLN. I found that for n = 10000000 the relative frequency was 0.167 for all the die rolls.  For this large value the program took a few seconds to run!

n = 100

# We create a list, dielist, containing die rolls.
dielist = rolldie(n)
print('Now we roll a die %i times.\n' % n)

# This for loop counts each die roll in the list and prints out the count and relative frequency for each number.
maxcount = 0
for i in range(1, 7):
    count = dielist.count(i)
    if count > maxcount:
        maxcount = count
    rf = count / float(n)
    print('There are %i %i\'s with a r. f. of %6.3f' % (count, i, rf))

# We should be able to predict how many rolls we need so that the r. f.'s of the die rolls agree to a chosen number of places.  We use the stand formula for the sample for a population proportion.   I used zc = 4 for the z-score associated with the level of confidence for the example.  I need to work out the level of confidence for z_c = 4.

z_c = 4
p = 1 / 6
E = 0.0005

samplesize = p * (1 - p) * (z_c / E) ** 2
print('\nThe sample size for agreement is%8.0f.' % samplesize)

# We add a histogram so we can visualize the result.

import matplotlib.pyplot as plt

# We adjust the maximum of y axis so the graphs look good for a wide range of n values.
max_y = maxcount + int(.20 * maxcount)

# Use the matplotlib to plot a histogram.  Note the graph approaches a uniform distribution as n increases providing a visual justification of the Law of Large Numbers.
plt.hist(dielist, bins=6)
plt.axis([1, 6, 0, max_y])
plt.show()

# This code is used instead of plt.show() when using PythonAnywhere since PA is browser-based.  See https://help.pythonanywhere.com/pages/MatplotLibGraphs/

# fig.savefig('diegraph.png')

# This code is necessary in PA if we get a Tkinter error when using matplotlib.
# matplotlib.use("Agg")
