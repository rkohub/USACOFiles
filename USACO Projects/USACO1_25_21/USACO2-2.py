import sys
import time
import math

start = time.time()

inn = """
5 4
1 3
1 2
2 3
2 4
"""

'''
linesArray = inn.split('\n')
del linesArray[-1]
del linesArray[0]
#'''

#linesArray = linesArray * 10000
#print(linesArray)

#for i in range(0,len(linesArray)):
	#linesArray[i] = linesArray[i].split()


#print(linesArray)
#print(time.time()-start)

#'''
linesArray = []
for line in sys.stdin:
    linesArray.append(line)
#'''

linesArray = [line.split() for line in linesArray]

pos = list(range(1,int(linesArray[0][0]) + 1))
startPos = pos
#print(pos)
seen = [int(math.pow(2,i-1)) for i in pos]
#print(seen)
#print(linesArray)
del linesArray[0]
#del linesArray[-1]


def swap(i,j):
	i -= 1
	j -= 1
	#print(i,j)
	seen[pos[i]-1] |= int(math.pow(2,j))
	seen[pos[j]-1] |= int(math.pow(2,i))

	store = pos[j]
	pos[j] = pos[i]
	pos[i] = store

def onesInBin(num):
	count = 0
	while(num > 0):
		if(num % 2 == 1):
			count += 1
		num >>= 1
	return count

def compileLoop():
	pass

def getAnswer():
	string = ""
	for i in seen:
		print(str(onesInBin(i)))
		#string += str(onesInBin(i)) + '\n'
		#print(string)


#print(linesArray)
#swap(1,3)

#for i in range(0,len(linesArray)):
	#swap(int(linesArray[i][0]),int(linesArray[i][1]))
	#seen[i] |= int(math.pow(2,j+1))print(pos)

#print(pos,seen)

while(time.time() < start + 3):
	for i in range(0,len(linesArray)):
		swap(int(linesArray[i][0]),int(linesArray[i][1]))
	#time.sleep(0.001)

getAnswer()