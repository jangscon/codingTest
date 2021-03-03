N = int(input())
NP = [0]*(N+1)

P = list(map(int , input().split()))
P.insert(0,0)
NP[1] = P[1]

for i in range(2 ,N + 1) :
    for j in range(1,i+1) :
        if NP[i-j] + P[j] > NP[i] :
            NP[i] =  NP[i-j] + P[j]
print(NP[N])

