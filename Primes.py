#This program implements the Sieve of Erastosthanes to generate all the primes from 2 to n
#By Alex Ambrioso (c)2018

#This function turns all the multiples of n in list to 0
def ZeroOut(list,n):
	for i in range(len(list)):
		if list[i]>n and list[i]%n==0:
			list[i]=0
	return list;

#The program creates a list from 2 to last.
#Then it calls ZeroOut to zero out all non-primes.  
#Finally, a list without the zeros is created and printed

last=1000 #Sets last element of list to be check for all primes
StartList=[i for i in range(2,last+1)] #Creates a list of the integers from 1 to last
for i in range(2,len(StartList)): 
	StartList=ZeroOut(StartList,i) #Iterates through the element of StartList
Primes=[]
for i in StartList:  #This loop creats the list of primes by removing all the zeros from StartList
	if i!=0:
		Primes.append(i)
print(Primes)

