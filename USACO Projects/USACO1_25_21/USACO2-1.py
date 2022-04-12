import sys

inn = """
4
3 3 1 1
1 1 3 1
3 3 1 1
1 1 3 3
"""

'''
linesArray = inn.split('\n')
del linesArray[-1]
del linesArray[0]
#'''

#'''
linesArray = []
for line in sys.stdin:
    linesArray.append(line)
#'''

del linesArray[0]
#print(linesArray)

for i in range(0,len(linesArray)):
	linesArray[i] = linesArray[i].split()
#print(linesArray)

rowOdds  = []
rowEvens = []

columnOdds  = []
columnEvens = []

for i in range(0,len(linesArray)):
	rowEvens.append(0)
	rowOdds.append(0)

	columnEvens.append(0)
	columnOdds.append(0)
	for j in range(0,len(linesArray)):
		if(j % 2 == 0):
			rowEvens[i] += int(linesArray[i][j])
			columnEvens[i] += int(linesArray[j][i])
		else:
			rowOdds[i] += int(linesArray[i][j])
			columnOdds[i] += int(linesArray[j][i])
#print(rowEvens, rowOdds)

# for j in range(0,len(linesArray)):
# 	columnEvens.append(0)
# 	columnOdds.append(0)
# 	for i in range(0,len(linesArray)):
# 		if(i % 2 == 0):
# 			columnEvens[j] += int(linesArray[i][j])
# 		else:
# 			columnOdds[j] += int(linesArray[i][j])
#print(columnEvens,columnOdds)

maxRows = maxCols = 0

for i in range(0,len(linesArray)):
	maxRows += max(rowOdds[i],rowEvens[i])
	maxCols += max(columnEvens[i],columnOdds[i])
#print(maxRows,maxCols)
ans = max(maxRows,maxCols)
print(ans)