from sys import stdin


alphabet = {}
inputStack =[]
stack = []

N = int(input())
I = list(str(stdin.readline().rstrip().split()))
for i in range(N) :
    inputStack.append(int(stdin.readline()))


for word in I :
    if word.isalpha() :
        if not alphabet.get(word) :
            alphabet[word] = inputStack.pop(0)
    if not inputStack :
        break

while I :
    current = I.pop(0)
    if current.isalpha() :
        stack.append(alphabet[current])
    else :
        if current == '+' :
            stack.append(stack.pop() + stack.pop())
        elif current == '-' :
            stack.append(stack.pop(-2) - stack.pop())
        elif current == '*' :
            stack.append(stack.pop() * stack.pop())
        elif current == '/' :
            stack.append(stack.pop(-2) / stack.pop())

print(f"{stack[0]:.2f}")
        
        