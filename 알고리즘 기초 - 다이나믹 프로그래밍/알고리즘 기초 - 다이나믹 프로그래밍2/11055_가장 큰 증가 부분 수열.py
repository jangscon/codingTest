n = int(input())
nums = [0] + list(map(int , input().split()))
dp = [0]*(n+1)
dp[1] = nums[1]

for i in range(2 , n+1) :
    max_num = 0
    for j in range(i, 0 , -1) :
        if nums[j] < nums[i] and max_num < dp[j]:
            max_num = dp[j]
    dp[i] = nums[i] + max_num
# print(dp)
print(max(dp))