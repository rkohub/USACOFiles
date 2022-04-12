#import numpy
#import statistics
#print("Hello World")

file = open("berries.in", 'r')
file = file.read()

#print(file)

linesArray = file.split("\n")
#print(linesArray)
del(linesArray[-1])
#print(linesArray)
linesArray = [linesArray[i].split() for i in range(0,len(linesArray))]
#print(linesArray)
linesArray = [int(linesArray[i][j]) for i in range(0,len(linesArray)) for j in range(0,len(linesArray[i]))]
#print(linesArray)

baskets = linesArray[1]
#print(f"Baskets {baskets}")

trees = linesArray[2:]
#print(trees)
#trees = numpy.asarray(trees)
#print(trees)
#trees = numpy.sort(trees)
trees.sort()
#print(trees)

#middleNum = trees[int(len(trees)/2)]
#print(middleNum)

subGroups = []
for i in range(1,trees[-1]+1):
    Sum = 0
    for j in range(0,len(trees)):
        Sum += int(trees[j]/i)
    subGroups.append(Sum)
#print(subGroups)
#print(round(statistics.mean(trees)))
index = 0
for i in range(0,len(subGroups)):
    if(subGroups[i] < baskets):
        index = i-1
        break
#print(index)












answer = int((index + 1)*(baskets/2))#8#int(middleNum * baskets/2)

answerStr = str(answer) + "\n"

#print(answerStr)
#'''
fileW = open("berries.out","w")
fileW.write(answerStr)
fileW.close()
#'''
