N = int(input())

Nums = []
for _ in range(N) :
    Nums.append(int(input()))

dp = [0,1,2,4] + [0]*8

for i in range(4 , 12) :
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for n in Nums :
    print(dp[n])
    