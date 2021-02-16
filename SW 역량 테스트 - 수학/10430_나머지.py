inputA ,inputB , inputC = input().split()

A = int(inputA)
B = int(inputB)
C = int(inputC)

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)