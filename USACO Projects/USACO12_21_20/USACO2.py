import sys

submit = False

if(submit):
	linesArray = []
	for line in sys.stdin:
		linesArray.append(line)

	inn = "".join(linesArray)
else:
	inn = """6
E 3 5
N 5 3
E 4 6
E 10 4
N 11 1
E 9 2
"""



linesArray = inn.split("\n")
# print(linesArray)
cows = linesArray[0]
blocked = [0] * int(cows)
del linesArray[0]
del linesArray[-1]
print(linesArray)

def sortCows():
	eastCows = []
	northCows = []
	for i in range(0,len(linesArray)):
		cow = linesArray[i].split()
		#print(cow)
		if(cow[0] == 'N'):
			northCows.append([int(cow[1]),int(cow[2])])
		else:
			eastCows.append([int(cow[1]),int(cow[2])])
	return northCows,eastCows

def showCows():
	print("N: " + str(NC))
	print("E: " + str(EC))

def step():
	addNorth()
	addEast()

def addNorth():
	for i in range(0,len(NC)):
		NC[i][1] += 1

def addEast():
	for i in range(0,len(EC)):
		EC[i][0] += 1

def printAnswer():
	for cow in blocked:
		print(cow)

NC, EC = sortCows()
showCows()
step()
showCows()

#printAnswer()