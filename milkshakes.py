#google code jam
#milkshakes problem
#https://code.google.com/codejam/contest/32016/dashboard#s=p1

import re

def method1(inputFile, outputFile):
	numCases = int(inputFile.readline())
		
	for case in range(numCases):
		flavors = int(inputFile.readline())
		customers = int(inputFile.readline())
		malted = [0 for x in range(flavors)]
		preferenceLists = list()
		for customer in range(customers):
			preferences = inputFile.readline()
			preferences = re.sub('\n', '', preferences)
			preferences = preferences.split(' ')
			preferences = list(map(int, preferences))
			thisCustomerPreferences = list()
			for flavor in range(preferences[0]):
				pair = (preferences[flavor*2 + 1], preferences[flavor*2 + 2])
				if pair[1] == 1:
					malted[pair[0]-1] = 1
				else:
					thisCustomerPreferences.append(pair[0]-1)
			if len(thisCustomerPreferences) > 0:
				preferenceLists.append(thisCustomerPreferences)
				
		canSucceed = True
		for preferenceList in preferenceLists:
			for flavor in preferenceList:
				if malted[flavor] == 0:
					break
			else:
				canSucceed = False
				break
		outString = 'Case #{}:'.format(case+1)
		if canSucceed:
			for flavor in range(len(malted)):
				outString = '{} {}'.format(outString, malted[flavor])
		else:
			outString = '{} IMPOSSIBLE'.format(outString)
		outputFile.write('{}\n'.format(outString))

if __name__ == '__main__':
	input = open(r'c:\users\adam\desktop\input.txt', 'r')
	output = open(r'c:\users\adam\desktop\output.txt', 'w')
	method1(input, output)
	input.close()
	output.close()