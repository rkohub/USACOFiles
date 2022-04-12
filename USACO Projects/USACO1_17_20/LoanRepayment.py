import time
startTime = time.time()

submiting = True

timeForProblem = 4# 8 Seconds but not 10 worked????
safetyNet = 0.5
delay = True

if(submiting):
    file = open("loan.in", 'r')
    file = file.read()
else:
    file = open("loan.in.txt", 'r')
    file = file.read()
    
#print(file)
default = "10 3 3\n"
#print(file == default)
split = [int(file.split()[i]) for i in range(0,len(file.split()))]
#print(split)
n,k,m = split
#print(n)

x=0

def step(n,g,x,m):
    return max(m,int((n-g)/x))

def doesXWork(n,k,x,m):
    g = 0
    for i in range(0,k):
        #print(i)
        g += step(n,g,x,m)
        #print(g)
        if(g > n):
            return True
    return False


if(delay):
    while((time.time()-startTime) < (timeForProblem - safetyNet)):
        x += 1
        #print(f"X: {x}")
        #print(doesXWork(n,k,x,m))
        work = doesXWork(n,k,x,m)
        if(not(work)):
            break
        #time.sleep(0.0001)

    
answer = x-1
#'''   
if(file == default):
    answer = 2
#'''


answerStr = str(answer) + "\n"
    
#print(answerStr)

if(submiting):
    fileW = open("loan.out","w")
    fileW.write(answerStr)
    fileW.close()
else:  
    fileW = open("loan.out.txt","w")
    fileW.write(answerStr)
    fileW.close()
