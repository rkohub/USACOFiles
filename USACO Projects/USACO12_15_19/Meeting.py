def returnCowPos(cow):
    return cow[1]

def updateCowPos(cowsArray, timePassed):
    for cow in cowsArray:
        cow[1] += (cow[2] * timePassed)
    return cowsArray

def smallestDifference(cowsArray):
    #assume Sorted
    leastDif = twoCowsDiff(cowsArray[0], cowsArray[1])
    for i in range(2,len(cowsArray)):
        dif = twoCowsDiff(cowsArray[i-1], cowsArray[i])
        if(dif == None):
            continue
        if(dif < leastDif):
            leastDif = dif
    return leastDif
        
def twoCowsDiff(cow1, cow2):
    if(cow1[2] == 0 or cow2[2] == 0):
        return cow2[1] - cow1[1]
    elif(cow1[2] == 1 and cow2[2] == -1):
        return (cow2[1] - cow1[1]) / (2.0)
    else:
        return None

def updateColision(cowsArray):
    for i in range(1,len(cowsArray)):
        if(cowsArray[i-1][1] == cowsArray[i][1]):
            if(cowsArray[i-1][2] == 0):
                weight = cowsArray[i][0]
                del cowsArray[i]
                return weight,cowsArray
            elif(cowsArray[i][2] == 0):
                weight = cowsArray[i-1][0]
                del cowsArray[i-1]
                return weight,cowsArray
            else:
                cowsArray[i-1][2] *= -1
                cowsArray[i][2] *= -1
                return 0, cowsArray

#'''
file = open("meetings.in", 'r')
file = file.read()
#'''

#print(file)
linesArray = file.split('\n')
#print(linesArray)
#THIS COULD BE THE PROBLEM
del linesArray[-1]
for i in range(0,len(linesArray)):
    linesArray[i] = linesArray[i].split()
#print(linesArray)
cowsArray = []
for i in range(1,len(linesArray)):
    cowsArray.append([])
    for j in range(0,len(linesArray[i])):
        cowsArray[i-1].append(int(linesArray[i][j]))

#print(cowsArray)
totalWeight = 0
for cow in cowsArray:
    totalWeight += cow[0]
#print("Total Weight: " + str(totalWeight))
barnPos = [0, int(linesArray[0][1])]
#Cow goes weight, position, direction
#print(barnPos)
#print("")
# Barns will be cows with weight 0 and movement 0
cowsArray.append([0,0,0])
cowsArray.append([0,barnPos[1],0])

totalWeightLost = 0
colisions = 0

while(totalWeightLost < totalWeight/2.0):
    cowsArray.sort(key = returnCowPos)
    #print(cowsArray)
    sd = smallestDifference(cowsArray)
    #print("SD: " + str(sd))
    cowsArray = updateCowPos(cowsArray, sd)
    #print(cowsArray)
    weightLost, cowsArray = updateColision(cowsArray)
    if(weightLost == 0):
        colisions += 1
    totalWeightLost += weightLost
    #print(cowsArray)
    #print(totalWeightLost)
    #print(colisions)

#print("FINAL COLITIONS: " + str(colisions))

answerString = str(colisions) + '\n'

#'''
fileW = open("meetings.out","w")
fileW.write(answerString)
fileW.close()
#'''
