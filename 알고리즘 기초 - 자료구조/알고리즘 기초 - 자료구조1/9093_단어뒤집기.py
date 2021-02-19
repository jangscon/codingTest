import sys

N = int(input())

outputString = ''

for i in range(N) :
    string = sys.stdin.readline().split()
    for j in string :
        if len(j) == 1 :
            outputString += j
        else : 
            for k in range(len(j)-1 , -1 , -1) :
                outputString += j[k]
        if j != len(string) - 1 :
            outputString += ' '
    print(outputString)
    outputString = ''
