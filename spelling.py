#google code jam
#store credit problem
#https://code.google.com/codejam/contest/351101/dashboard#s=p2

import re

def run(inputFile, outputFile):
	keypadDict = {
		'a':'2',
		'b':'22',
		'c':'222',
		'd':'3',
		'e':'33',
		'f':'333',
		'g':'4',
		'h':'44',
		'i':'444',
		'j':'5',
		'k':'55',
		'l':'555',
		'm':'6',
		'n':'66',
		'o':'666',
		'p':'7',
		'q':'77',
		'r':'777',
		's':'7777',
		't':'8',
		'u':'88',
		'v':'888',
		'w':'9',
		'x':'99',
		'y':'999',
		'z':'9999',
		' ':'0'
	}

	numCases = int(inputFile.readline())
	
	for case in range(numCases):
		phrase = inputFile.readline()
		phrase = re.sub('\n', '', phrase)
		phrase = phrase.lower()
		previousCode = '1'
		outputLine = ''
		for char in phrase:
			code = keypadDict[char]
			if code[0] == previousCode:
				outputLine = '{} '.format(outputLine)
			previousCode = code[0]
			outputLine = '{0}{1}'.format(outputLine, code)
		outputFile.write('Case #{0}: {1}\n'.format(case+1, outputLine))
	
if __name__ == '__main__':
	input = open(r'c:\users\adam\desktop\input.txt', 'r')
	output = open(r'c:\users\adam\desktop\output.txt', 'w')
	run(input, output)
	input.close()
	output.close()