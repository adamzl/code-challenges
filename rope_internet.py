#google code jam
#rope internet problem
#https://code.google.com/codejam/contest/619102/dashboard#s=p0

import re

def method1(inputFile, outputFile):
	numCases = int(inputFile.readline())
		
	for case in range(numCases):
		numWires = int(inputFile.readline())
		wireList = list()
		for wire in range(numWires):
			input = inputFile.readline()
			input = re.sub('\n', '', input)
			input = input.split(' ')
			wireList.append((int(input[0]), int(input[1])))
		
		intersections = 0
		for wireNum in range(numWires-1):
			wire = wireList[wireNum]
			for otherWire in wireList[wireNum+1:]:
				if wire[0] < otherWire[0] and wire[1] > otherWire[1]:
					intersections += 1
				elif wire[0] > otherWire[0] and wire[1] < otherWire[1]:
					intersections += 1
		
		outputFile.write('Case #{0}: {1}\n'.format(case+1, intersections))
		print('{} / {}'.format(case+1, numCases))
		
def method2(inputFile, outputFile):
	numCases = int(inputFile.readline())
		
	for case in range(numCases):
		numWires = int(inputFile.readline())
		wireList = list()
		for wire in range(numWires):
			input = inputFile.readline()
			input = re.sub('\n', '', input)
			input = input.split(' ')
			wireList.append((int(input[0]), int(input[1])))
		
		intersections = 0
		for wireNum in range(numWires-1):
			wire = wireList[wireNum]
			for otherWire in wireList[wireNum+1:]:
				if ((wire[0] - otherWire[0]) * (wire[1] - otherWire[1])) < 0:
					intersections += 1
		
		outputFile.write('Case #{0}: {1}\n'.format(case+1, intersections))
		print('{} / {}'.format(case+1, numCases))

if __name__ == '__main__':
	input = open(r'c:\users\adam\desktop\input.txt', 'r')
	output = open(r'c:\users\adam\desktop\output.txt', 'w')
	#method1(input, output)
	method2(input, output)
	input.close()
	output.close()