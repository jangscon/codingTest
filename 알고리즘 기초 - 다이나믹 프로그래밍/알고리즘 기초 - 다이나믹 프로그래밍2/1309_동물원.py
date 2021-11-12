n = int(input())
DP = [1,1,1]

for i in range(1,n) :
    zero = DP[1] + DP[2] + DP[0]
    one = DP[2] + DP[0]
    two = DP[1] + DP[0]
    DP = [zero,one,two]

print(sum(DP)%9901)