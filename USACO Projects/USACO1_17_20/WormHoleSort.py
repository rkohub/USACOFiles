import time
startTime = time.time()

submiting = True

timeForProblem = 4# 8 Seconds but not 10 worked????
safetyNet = 0.5
delay = True

if(submiting):
    file = open("wormsort.in", 'r')
    file = file.read()
else:
    file = open("wormsort.in.txt", 'r')
    file = file.read()
    

#linesArray = file.split("\n")
#print(linesArray)
linesArray = file.split("\n")[:-1]
#print(linesArray)
dataArray = []
for i in range(0,len(linesArray)):
    dataArray.append([])
    line = linesArray[i].split()
    if(i > 1):
        for j in range(0,len(line)):
            dataArray[i].append(int(line[len(line)-1-j]))
    else:
        for j in range(0,len(line)):
            dataArray[i].append(int(line[j]))
#print(dataArray)

cowPos = dataArray[1]
#print(cowPos)

wrongPlace = []
for i in range(0,len(cowPos)):
    if(not(cowPos[i] == i+1)):
        wrongPlace.append(i+1)
#print(wrongPlace)

if(len(wrongPlace) == 0):
    answer = -1
    answerStr = str(answer) + "\n"
    if(submiting):
        fileW = open("wormsort.out","w")
        fileW.write(answerStr)
        fileW.close()
    else:  
        fileW = open("wormsort.out.txt","w")
        fileW.write(answerStr)
        fileW.close()
else:    
    holes = dataArray[2:]
    #print(holes)
    holes.sort(reverse = True)
    #print(holes)
    wrongPlace = set(wrongPlace)
    #print(wrongPlace)
    #for k in range(1,len(holes)):
    k = 0
    #print(holes[k-1][0])        
    

    if(delay):
        while((time.time()-startTime) < (timeForProblem - safetyNet) and k < len(holes)):
            k += 1
            links = []
            for i in range(0,k):
                hole = holes[i]
                add = False
                for j in range(0, len(links)):
                    link = links[j]
                    if(hole[1] in link):
                        add = True
                        if(hole[2] not in link):
                            link.update({hole[2]})
                    if(hole[2] in link):
                        add = True
                        if(hole[1] not in link):
                            link.update({hole[1]})
                if(not add):
                    links.append(set(hole[1:]))
            #print(f"L: {links}")
            restart = True
            while(restart):
                restart = False
                for i in range(0, len(links)):
                    if(restart):
                        break
                    link1 = links[i]
                    for j in range(i+1, len(links)):
                        if(restart):
                            break
                        link2 = links[j]
                        #print(f"L1: {link1}, L2: {link2}")
                        if(not(link1.isdisjoint(link2))):
                            links[i] = link1.union(link2)
                            #print(f"L1: {link1}, L2: {link2}")
                            del links[j]
                            restart = True
            #print(f"L: {links}")
            done = False
            for link in links:
                if(wrongPlace.issubset(link)):
                    done = True
            if(done):
                break
            
            #time.sleep(0.0001)

        
    answer = holes[k-1][0]

    answerStr = str(answer) + "\n"
        
    #print(answerStr)

    if(submiting):
        fileW = open("wormsort.out","w")
        fileW.write(answerStr)
        fileW.close()
    else:  
        fileW = open("wormsort.out.txt","w")
        fileW.write(answerStr)
        fileW.close()
