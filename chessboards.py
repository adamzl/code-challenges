#google code jam
#making chessboards problem
#https://code.google.com/codejam/contest/619102/dashboard#s=p2

import re

eBlack = 0
eWhite = 1
def switch(cell):
	if cell == eBlack:
		return eWhite
	if cell == eWhite:
		return eBlack
	raise Exception()

def method1(inputFile, outputFile):
	numCases = int(inputFile.readline())
		
	for case in range(numCases):
		dimensions = inputFile.readline()
		dimensions = re.sub('\n', '', dimensions)
		dimensions = dimensions.split(' ')
		rows = int(dimensions[0])
		cols = int(dimensions[1])
		bark = [[eBlack for col in range(cols)] for row in range(rows)]
		for rowNum in range(rows):
			rowData = int(inputFile.readline(), base=16)
			for colNum in range(cols):
				andValue = pow(2, colNum)
				bitValue = rowData & andValue
				if bitValue > 0:
					bark[rowNum][cols - colNum - 1] = eWhite
					
		rowRuns = [[1 for col in range(cols)] for row in range(rows)]
		colRuns = [[1 for col in range(cols)] for row in range(rows)]
		for row in range(rows-1,-1,-1):
			for col in range(cols-2,-1,-1):
				if bark[row][col] != bark[row][col+1]:
					rowRuns[row][col] = rowRuns[row][col+1]+1
		for col in range(cols-1,-1,-1):
			for row in range(rows-2,-1,-1):
				if bark[row][col] != bark [row+1][col]:
					colRuns[row][col] = rowRuns[row+1][col]+1
		
		boards = [[0 for col in range(cols)] for row in range(rows)]
		for row in range(0,rows):
			for col in range(0,cols):
				boardSize = min(rowRuns[row][col], colRuns[row][col])
				if boards[row][col] < boardSize:
					for subrow in range(row,row+boardSize):
						for subcol in range(col,col+boardSize):
							boards[row][col] = boardSize
		
		largestBoard = 0
		for boardSize in range(len(boardCounts)-1, 0, -1):
			if boardCounts[boardSize] > 0:
				largestBoard = boardSize
				break
		print('Case #{}: {}'.format(case+1, largestBoard))
		for boardSize in range(largestBoard, -1, -1):
			print('{} {}'.format(boardSize, boardCounts[boardSize]))

if __name__ == '__main__':
	input = open(r'c:\users\adam\desktop\input.txt', 'r')
	output = open(r'c:\users\adam\desktop\output.txt', 'w')
	method1(input, output)
	input.close()
	output.close()