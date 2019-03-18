
str='Alexander'
tup=tuple(str)

for i in tup:
    print(tup.count(i))

import bisect

list = [1,2,3,10,10,11,12,33,45,58]
print(bisect.insort(list,57))
print(list)
