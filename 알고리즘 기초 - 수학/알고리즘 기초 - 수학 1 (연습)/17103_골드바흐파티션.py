T = int(input())

N = []
result = []

for i in range(T) :
    N.append(int(input()))

bigger = max(N)
prime = [False]*2 + [True]*(bigger-1)

for i in range(2,bigger+1) :
    if prime[i] :
        num = i*2
        while num <= bigger :
            prime[num] = False 
            num = num + i

while N :
    num = N.pop(-1)
    temp = 2
    count = 0
    while temp <= num // 2 :
        if prime[temp] and prime[num - temp] : count += 1
        temp += 1
    result.append(count)

result = reversed(result)
for i in result :
    print(i)
    
