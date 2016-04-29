#google code jam
#alien language problem
#https://code.google.com/codejam/contest/90101/dashboard#s=p0

import re

class treeTier:
	def __init__(self, sublist):
		sublist.sort()
		self.branches = dict()
		if len(sublist[0]) == 1:
			for letter in sublist:
				self.branches[letter] = None
		else:
			for word in sublist:
				letter = word[0]
				if letter not in self.branches:
					self.branches[letter] = list()
				self.branches[letter].append(word[1:])
			for key,value in self.branches.items():
				self.branches[key] = treeTier(value)

def buildTree(inputFile, wordLength, wordCount):
	listOfWords = list()
	for a in range(wordCount):
		line = inputFile.readline()
		line = re.sub('\n', '', line)
		listOfWords.append(line)
	return treeTier(listOfWords)

def searchLetters(tree, letters):
		if letters[0] == '(':
			match = re.match(r'(\(.*?\))(.*)', letters)
			lettersToSearch = match.group(1)
			lettersToSearch = lettersToSearch[1:len(lettersToSearch)-1]
			remainder = match.group(2)
			sumOfFinds = 0
			for letter in lettersToSearch:
				if letter in tree.branches:
					if tree.branches[letter] is None:
						sumOfFinds += 1
					else:
						sumOfFinds += searchLetters(tree.branches[letter], remainder)
			return sumOfFinds
		else:
			if letters[0] in tree.branches:
				if tree.branches[letters[0]] is None:
					return 1
				else:
					return searchLetters(tree.branches[letters[0]], letters[1:])
			return 0

def method1(inputFile, outputFile):
	inputLine = inputFile.readline()
	match = re.match(r'(\d+) (\d+) (\d+)', inputLine)
	wordLength = int(match.group(1))
	wordCount = int(match.group(2))
	messageCount = int(match.group(3))
	
	tree = buildTree(inputFile, wordLength, wordCount)
	for case in range(messageCount):
		message = inputFile.readline()
		message = re.sub('\n', '', message)
		count = searchLetters(tree, message)
		outputFile.write('Case #{}: {}\n'.format(case+1, count))
		print('Case #{}: {}'.format(case+1, count))

def method2(inputFile, outputFile):
	inputLine = inputFile.readline()
	match = re.match(r'(\d+) (\d+) (\d+)', inputLine)
	wordLength = int(match.group(1))
	wordCount = int(match.group(2))
	messageCount = int(match.group(3))
	
	dictionary = ''
	for word in range(wordCount):
		word = inputFile.readline()
		word = re.sub('\n', '', word)
		dictionary = '{} {}'.format(dictionary, word)
	for case in range(messageCount):
		regex = inputFile.readline()
		regex = re.sub('\n', '', regex)
		regex = re.sub('\(', '[', regex)
		regex = re.sub('\)', ']', regex)
		matches = re.findall(regex, dictionary)
		outputFile.write('Case #{}: {}\n'.format(case+1, len(matches)))
		print('Case #{}: {}'.format(case+1, len(matches)))

if __name__ == '__main__':
	input = open(r'c:\users\adam\desktop\input.txt', 'r')
	output = open(r'c:\users\adam\desktop\output.txt', 'w')
	#method1(input, output)
	method2(input, output)
	input.close()
	output.close()