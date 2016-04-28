#google code jam
#store credit problem
#https://code.google.com/codejam/contest/351101/dashboard#s=p1

import re

def run(inputFile, outputFile):
	numCases = int(inputFile.readline())
	
	for case in range(numCases):
		words = inputFile.readline()
		words = re.sub('\n', '', words)
		words = words.split(' ')
		words.reverse()
		newLine = ''
		for word in words:
			newLine = ('{} {}'.format(newLine, word))
		output.write('Case #{0}:{1}\n'.format(case+1, newLine))
		

if __name__ == '__main__':
	input = open(r'c:\users\adam\desktop\input.txt', 'r')
	output = open(r'c:\users\adam\desktop\output.txt', 'w')
	run(input, output)
	input.close()
	output.close()