n = int(input())
nums = [1001] + list(map(int , input().split()))
dp = [1 for _ in range(n+1)]
dp[0] = 0
dp[1] = 1
for i in range(n+1) :
    count = 0
    for j in range(i , 0 , -1) :
        if nums[j] > nums[i] and count < dp[j] :
            count = dp[j]
    dp[i] += count
# print(dp)
print(max(dp))

