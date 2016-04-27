#google code jam
#store credit problem
#https://code.google.com/codejam/contest/351101/dashboard#s=p0

def naive(inputFile, outputFile):
	numCases = int(inputFile.readline())
	
	for case in range(numCases):
		credits = int(inputFile.readline())
		
		inputFile.readline() #eat the number of items
		
		items = inputFile.readline()
		items = items.split(' ')
		items = list(map(int, items))
		
		found = False
		for a in range(len(items)):
			if found:
				break
			for b in range(len(items)):
				if a == b:
					continue
				if items[a] + items[b] == credits:
					found = True
					outputFile.write('Case #{0}: {1} {2}\n'.format(case+1, a+1, b+1))
					break

def linear(inputFile, outputFile):
	numCases = int(inputFile.readline())
		
	for case in range(numCases):
		credits = int(inputFile.readline())
		
		inputFile.readline() #eat the number of items
		
		items = inputFile.readline()
		items = items.split(' ')
		items = list(map(int, items))
		
		itemsTuple = list()
		counter = 0
		for item in items:
			itemsTuple.append((item, counter))
			counter += 1
		items = itemsTuple
		items.sort(key=lambda tuple: tuple[0])
		
		left = 0
		right = len(items)-1
		
		while items[left][0] + items[right][0] != credits:
			total = items[left][0] + items[right][0]
			if total < credits:
				left += 1
			else:
				right -= 1
				
		if items[left][1] > items[right][1]:
			temp = left
			left = right
			right = temp
		outputFile.write('Case #{0}: {1} {2}\n'.format(case+1, items[left][1]+1, items[right][1]+1))

if __name__ == '__main__':
	input = open(r'c:\users\adam\desktop\input.txt', 'r')
	output = open(r'c:\users\adam\desktop\output.txt', 'w')
	#naive(input, output)
	linear(input, output)
	input.close()
	output.close()