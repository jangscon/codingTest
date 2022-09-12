# N = int(input())
# A = list(map(int , input().split()))
# dp = [0 for _ in range(N)]
# dp[0] = A[0]
# result = 0
# for i in range(N) :
#     for j in range(i) :
#         if dp[i]
#

T = int(input())
test = []
for i in range(T) :
    test.append(list(map(float , input().split())))
isright = False
spot = 0
sum = 0

for j in test :
    jump = j[1]
    count = 1
    while sum < j[0] :
        isright = not isright
        sum += jump*count
        spot += jump*count if isright else -jump*count
        count += 1
    spot += (-(sum - j[0] +1)) if isright else sum - j[0] +1
    print(int(spot) ,end="")
    print(" R" if isright else " L")
    spot = 0
    sum = 0
    isright = False