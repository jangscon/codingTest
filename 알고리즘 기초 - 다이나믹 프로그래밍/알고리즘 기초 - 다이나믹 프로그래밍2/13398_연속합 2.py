n = int(input())
seq = [0]+list(map(int , input().split()))

result = [[0 for _ in range(n+1)] for _ in range(2)]
result[0][1] = seq[1]
result[1][1] = seq[1]

for i in range(2 , n+1) :
    result[0][i] = max(seq[i] + result[0][i-1] , seq[i])
    result[1][i] = max(seq[i] + result[1][i-1] , result[0][i-1])

# print(result[0])
# print(result[1])
print(max(max(result[0][1:]),max(result[1][1:])))
