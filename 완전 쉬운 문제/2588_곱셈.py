inputA = input()
inputB = input()
A = int(inputA)
B = int(inputB)

oneB = B%10
tenB = int(B/10)%10
hunB = int(int(B/10)/10)
print(A*oneB)
print(A*tenB)
print(A*hunB)
print(A*B)