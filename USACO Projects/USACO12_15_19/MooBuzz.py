def mooBuzz(num):
    if(num <= 0):
        return 0
    counter = 0
    i = 1
    while(True):
        if(not(i % 3 == 0 or i % 5 == 0)):
            counter += 1
            if(counter == num):
                return i
        i += 1


#'''
file = open("moobuzz.in","r")
file = file.read()
testFile = file
#'''

#testFile = "1000\n"

num = int(testFile)

#print(testFile)
#print(num + 1)
mod = num % 8
#print(mod)

answer = (int(num/8) * 15) + (mooBuzz(mod))
if(mod == 0):
    answer -= 1
#print("Answer: " + str(answer))
#print("Answer: " + str(mooBuzz(num)))

answerString = str(answer) + '\n'


#'''
fileW = open("moobuzz.out","w")
fileW.write(answerString)
fileW.close()
#'''
