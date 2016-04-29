#google code jam
#minimum scalar product problem
#https://code.google.com/codejam/contest/32016/dashboard#s=p0

import re

def linear(inputFile, outputFile):
	numCases = int(inputFile.readline())
		
	for case in range(numCases):
		inputFile.readline() #eat the input count
		vector1 = inputFile.readline()
		vector2 = inputFile.readline()
		vector1 = re.sub('\n', '', vector1)
		vector2 = re.sub('\n', '', vector2)
		vector1 = vector1.split(' ')
		vector2 = vector2.split(' ')
		vector1 = list(map(int, vector1))
		vector2 = list(map(int, vector2))
		vector1.sort()
		vector2.sort(reverse=True)
		
		sum = 0
		for x in vector1:
			sum += x * vector2.pop(0)
			
		outputFile.write('Case #{0}: {1}\n'.format(case+1, sum))

if __name__ == '__main__':
	input = open(r'c:\users\adam\desktop\input.txt', 'r')
	output = open(r'c:\users\adam\desktop\output.txt', 'w')
	linear(input, output)
	input.close()
	output.close()