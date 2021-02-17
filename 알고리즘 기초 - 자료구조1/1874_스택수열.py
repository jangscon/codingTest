import sys 

N = int(input())

numlist = []
numlistIndex = 0 
currentNum = 1
stack = []
output = ''

for i in range(N) :
    numlist.append(int(sys.stdin.readline()))

while numlistIndex < N-1 :
    if currentNum == numlist[numlistIndex] :
        currentNum += 1
        numlistIndex += 1
        output += '+-'
    
    elif currentNum < numlist[numlistIndex] :
        stack.append(currentNum)
        currentNum += 1
        output += '+'

    elif stack :
        if stack[-1] == numlist[numlistIndex] :
            stack.pop()
            numlistIndex += 1
            output += '-'
        elif stack[-1] > numlist[numlistIndex] :
            break
if currentNum == N+1 and numlistIndex == N-1:
    for i in output :
        print(i)
    print('-')
if N == 1 :
    print('+')
    print('-')
else :
    print('NO')
