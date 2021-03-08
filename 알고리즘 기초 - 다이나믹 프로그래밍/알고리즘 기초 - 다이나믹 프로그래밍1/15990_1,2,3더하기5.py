N = int(input())

nums = [int(input()) for _ in range(N)]

np = [[0]*3 for _ in range(max(nums)+1)]
np[1] = [1,0,0]
np[2] = [0,1,0]
np[3] = [1,1,1]

for i in range(4,max(nums)+1) :
    np[i][0] = (np[i-1][1] + np[i-1][2])%1000000009
    np[i][1] = (np[i-2][0] + np[i-2][2])%1000000009
    np[i][2] = (np[i-3][0] + np[i-3][1])%1000000009

for i in nums :
    result = sum(np[i])%1000000009
    print(result)

