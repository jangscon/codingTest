N = int(input())
A = list(map(int , input().split()))
dp = [0 for _ in range(N)]

for i in range(N) :
    for j in range(i) :
        if A[j] < A[i] and dp[i] < dp[j] :
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
order = max(dp)
lst = []
for i in range(N-1, -1, -1):
    if dp[i]==order:
        lst.append(A[i])
        order-=1
lst.reverse()
for i in lst:
    print(i, end=' ')