import math
import sys
# import numpy as np

# inn = str(sys.stdin)
# print(inn)
# # inn = input()
# # inn = """4
# # 4 1
# # 1 3
# # 3 2
# # """

# inn = """4
# 4 1
# 1 3
# 3 2
# """

# # #print(inn)
# linesArray = inn.split()
# print(lin)
# del linesArray[-1]


linesArray = []
for line in sys.stdin:
	linesArray.append(line)

# linesArray = ["4\n", "1 2\n", "1 3\n", "1 4\n"]
inn = "".join(linesArray)

# print("".join(linesArray))

# print(linesArray[1])
linesArray = inn.split()


leaves = int(linesArray[0])
#print(leaves)
#print(type(linesArray[1]))

# lines = np.array(linesArray[1:])
lines = linesArray[1:]
# print(lines)

newLines = []
block = []
for i in range(0, len(lines)):
	block.append(lines[i])
	if(i % 2 == 1):
		newLines.append(block)
		block = []
	# print(i)
# print(newLines)
lines = newLines
# lines = np.reshape(lines, (-1, 2))
# print(lines)

def findOccurances(arr, val):
	occurances = []
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			if(val == arr[i][j]):
				occurances.append([i,j])
	return occurances

def arrayAtArray(arr, indexArr):
	ret = []
	for item in indexArr:
		#print(item)
		#print(arr[0][0])
		ret.append(arr[item[0]][(item[1]+1)%2])
	return ret

def findConnectedLeafs(nodeNum, cameFromNode):
	# connections = np.where(str(nodeNum) == lines)
	occ = findOccurances(lines, str(nodeNum))

	connections = arrayAtArray(lines, occ)


	#print(connections)

	# connections = lines[connections[0], (connections[1] + 1) % 2]

	if(cameFromNode != -1):
		connections = list(connections)
		ind = connections.index(str(cameFromNode))
		del connections[ind]

	# print(connections)
	# print(connections.size)
	return connections

def movesForLeafs(leafCount):
	#Moves = dups + leaves
	#dups = celing(logbase2(leaves + 1)))
	return math.ceil(math.log(leafCount + 1,2)) + leafCount

moves = 0
def findMoveCount(nodeNum = 1, cameFromNode = -1):
	# print(nodeNum, cameFromNode)
	cons = findConnectedLeafs(nodeNum,cameFromNode)
	if(len(cons) <= 0):
		# print("LEAFING")
		return
	global moves
	moves += movesForLeafs(len(cons))
	# print("MOVES IS NOW: " + str(moves))
	for con in cons:
		findMoveCount(int(con), nodeNum)

findMoveCount()
print(moves)

# print(findConnectedLeafs(1,4))

