n = int(input())
wine = [0]
for i in range(n) :
    wine.append(int(input()))
DP = [0]
DP.append(wine[1])
if n > 1 :
    DP.append(DP[1] + wine[2])

for i in range(3,n+1) :
    DP.append(max(wine[i] + wine[i-1] + DP[i-3] , wine[i] + DP[i-2] , DP[i-1]))


print(max(DP))
