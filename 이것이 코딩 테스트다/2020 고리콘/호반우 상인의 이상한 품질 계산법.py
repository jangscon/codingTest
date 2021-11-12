N = int(input())
hovanu = list(map(int ,input().split()))
hovanu.sort()
result = 0
# print(hovanu)

if N == 1 :
    print(hovanu[0])
else :
    hovanu_range = N//2
    for i in range(hovanu_range) :
        # print(hovanu[N-1-i])
        result += hovanu[N-1-i] * 2
    if N % 2 == 1 :
        result += hovanu[hovanu_range]
    print(result)
