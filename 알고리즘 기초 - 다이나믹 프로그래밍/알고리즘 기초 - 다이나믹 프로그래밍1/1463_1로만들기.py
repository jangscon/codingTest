# 보텀 업 방식으로 1부터 시작해서 입력한 N이 될때 까지 1씩 더하고 
# 만약 현재 인덱스가 2 혹은 3으로 나눠 떨어지면 
# 2 or 3으로 나눈 인덱스의 값과 이전 값에 1을 더한 값과 비교해서 
# 더 낮은 값으로 dp의 값을 정한다.

N = int(input())

dp = [0]*(N+1)

for i in range(2 , N+1) :
    dp[i] = dp[i-1] + 1
    if i % 2 == 0 and dp[i//2] + 1 < dp[i] : 
        dp[i] = dp[i//2] + 1
    if i % 3 == 0 and dp[i//3] + 1 < dp[i] : 
        dp[i] = dp[i//3] + 1
    
print(dp[N])