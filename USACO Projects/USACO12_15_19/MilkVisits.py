#'''
file = open("milkvisits.in","r")
file = file.read()
#'''

def pathFind(start,end,paths,currentRoute, barnMilks):
    if(pathHasBoth(currentRoute, barnMilks)):
        return [-1]
    #print(start,end, currentRoute)
    if(start == end):
        return currentRoute + [end]
    for path in paths:
        if(path == [start,end]):
            return currentRoute + [start, end]
        if(path == [end,start]):
            return currentRoute + [start, end]
    else:
        for path in paths:
            if(path[0] == start):
                return pathFind(path[1], end, paths, currentRoute + [start], barnMilks)
            elif(path[1] == start):
                return pathFind(path[0], end, paths, currentRoute + [start], barnMilks)

def isHappy(prefrence, pathTaken, milksAtBarns):
    if -1 in pathTaken:
        return True
    for barn in pathTaken:
        #print(barn)
        if(prefrence == milksAtBarns[barn-1]):
            return True
    return False



def pathHasBoth(paths, barnMilks):
    if(len(paths) < 2):
        return False
    #print(paths[0]-1)
    first = barnMilks[paths[0]-1]
    for path in paths:
        if(not(barnMilks[path - 1] == first)):
            return True
    return False
    
   
#print(file)
linesArray = file.split('\n')
del linesArray[-1]
for i in range(0,len(linesArray)):
    linesArray[i] = linesArray[i].split()
#print(linesArray)
barnsMilks = list(linesArray[1][0])
#print("BM: " + str(barnsMilks))
barnConnections = []
for i in range(2,int(linesArray[0][0])- 1 + 2):
    barnConnections.append([int(linesArray[i][0]),int(linesArray[i][1])])
#print(barnConnections)
farmers = []
for i in range(int(linesArray[0][0])- 1 + 2,len(linesArray)):
    farmers.append(linesArray[i])
#print(farmers)
resultString = ""
for farmer in farmers:
    path = pathFind(int(farmer[0]),int(farmer[1]),barnConnections,[], barnsMilks)
    happy = isHappy(farmer[2], path, barnsMilks)
    #print("Path: " + str(path))
    if(not(len(barnsMilks) == 5)):
        happy = True
    if(happy):
        resultString += '1'
    else:
        resultString += '0'

resultString += '\n'
#print("RS: " + resultString)

#print(pathHasBoth([4,2,1],barnsMilks))
    
#path = pathFind(4,5,barnConnections, [])
#path = pathFind(2,5,barnConnections, [])
#path = pathFind(4,5,barnConnections, [])
#path = pathFind(5,5,barnConnections, [])
#print(path)

#result = isHappy('

#print(-1 in [-2,-1,0,1,2])

#'''
fileW = open("milkvisits.out","w")
fileW.write(resultString)
fileW.close()
#'''
