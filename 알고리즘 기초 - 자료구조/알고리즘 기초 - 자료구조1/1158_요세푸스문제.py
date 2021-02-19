from sys import stdin   

N , K = map(int , stdin.readline().rstrip().split())

array = [i for i in range(1 ,N + 1)]
output = []
temp = K - 1

for i in range(N) : 
    if temp < len(array) :
        output.append(array.pop(temp))
        temp += K-1
    elif temp >= len(array) :
        temp = temp % len(array) 
        output.append(array.pop(temp))
        temp += K-1

    
print('<',end="")
for i in output :
    print(i ,end="")
    if i != output[-1] :
        print(", " ,end="")
print('>')