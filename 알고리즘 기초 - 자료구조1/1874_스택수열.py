import sys 

N = int(input())

inputString = []
Index = 0
NoStack = False
stack = []
output = []

for i in range(N) :
    inputString.append(int(sys.stdin.readline()))

for i in range(1, N+1) :
    stack.append(i)
    output.append('+')

    while stack :
        if stack[-1] == inputString[Index] :
            stack.pop()
            Index += 1
            output.append('-') 
        elif stack[-1] > inputString[Index] :
            NoStack = True
            break
        else :
            break
 
    if NoStack :
        break

if NoStack or stack:
    print('NO')
else :
    for word in output :
        print(word)