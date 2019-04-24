import numpy

matrix = numpy.zeros(shape=(12,12), dtype=int)

s = [[str(e) for e in row] for row in matrix]

lens = [max(map(len, col)) for col in zip(*s)]

fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]

for i in range(3):
    matrix[i,i**2]=-1

print(matrix)
