N = int(input())
NP = [0]*(N+1)
P = list(map(int , input().split()))
P.insert(0,0)
NP[1] = P[1]

for i in range(2 , N+1) :
    NP[i] = P[i]
    for j in range(1,i+1) :
        if NP[i] > NP[i-j] + NP[j] :
            NP[i] = NP[i-j] + NP[j]
print(NP[N])