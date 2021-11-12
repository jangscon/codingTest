n = int(input())
consult = [(0,0)]
for _ in range(n) :
    consult.append(tuple(map(int , input().split())))
DP = [0 for _ in range(n+1)]
DP.append(0)

for i in range(1,n+1) :
    if i+consult[i][0] <= n+1 :
        DP[i] = consult[i][1]
        for j in range(1,i+1) :
            if consult[j][0] + j - 1 < i and DP[i] < DP[j] + consult[i][1] :
                DP[i] = DP[j] + consult[i][1]


# print(consult[1:])
# print(DP[1:])
print(max(DP))