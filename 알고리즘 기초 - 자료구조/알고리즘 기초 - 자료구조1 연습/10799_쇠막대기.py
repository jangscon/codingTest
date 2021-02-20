from sys import stdin 

inputList = list(stdin.readline().rstrip())

stack = 0
output = 0

while True :
    if not inputList and stack == 0:
        break
    inputWord = inputList.pop(0)
    if inputWord == '(' :
        if inputList[0] == ')' :
            inputList.pop(0)
            output += stack
        else :
            stack += 1
    else :
        output += 1
        stack -= 1
        
print(output)