#This program implements the Sieve of Erastosthanes to generate all the primes from 2 to n
#By Alex Ambrioso (c)2018

import math

#This function turns all the multiples of n in list that are greater then n to 0
def ZeroOut(list,n):
	for i in range(len(list)):
		if list[i]>n and list[i]%n==0:
			list[i]=0
	return list;

#Try it!

list2 = ZeroOut([1,2,3,4,5,6,7,8,9,10], 3)
print(list2)

#The function creates a list from 2 to last.
#Then it calls ZeroOut to zero out all non-primes.
#Finally, a list without the zeros is created and output

def Primes(n):
    last=n #Sets last element of list to be check for all primes
    StartList=[i for i in range(2,last+1)] #Creates a list of the integers from 1 to last
    for i in range(2,len(StartList)):
        StartList=ZeroOut(StartList,i) #Iterates through the element of StartList
    Primes=[]
    for i in StartList:  #This loop creats the list of primes by removing all the zeros from StartList
        if i!=0:
            Primes.append(i)
    return Primes

print(Primes(100))

def isPrime(n):
    check = math.sqrt(n)
    last=int(check)
    checklist = Primes(last)
    print(last, checklist)
    for i in checklist:
        if n % i == 0:
            return False
    return True


print(isPrime(47))
