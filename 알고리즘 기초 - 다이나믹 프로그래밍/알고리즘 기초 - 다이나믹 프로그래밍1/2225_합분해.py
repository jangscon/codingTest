n , k = map(int , input().split())
DP = [[1]*(n+1) for i in range(k)]
DP.insert(0,[0]*(n+1))

for i in range(1 , k+1) :
    for j in range(1 , n+1) :
        DP[i][j] = DP[i-1][j] + DP[i][j-1]
print(DP[k][n] % 1000000000)