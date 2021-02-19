from sys import stdin 

S = list(stdin.readline().rstrip())

stack = []
output = ''


while True :
    if not S :
        output += ''.join(reversed(stack))
        stack = []
        break

    word = S.pop(0)

    if word == '<' :
        if stack :
            output += ''.join(reversed(stack))
            stack = []
        stack.append(word)
        while True :
            stack.append(S.pop(0))
            if stack[-1] == '>':
                output += ''.join(stack)
                stack = []
                break
        continue
    elif word == ' ' :
        if stack :
            output += ''.join(reversed(stack))
            stack = []
        output += ' '
        continue
    else : 
        stack.append(word)
        continue

print(output)

        

            
             