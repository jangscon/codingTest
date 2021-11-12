N = int(input())
result = []
for i in range(N) :
    result.append(int(input()))
result = sorted(result , reverse=True)
print(' '.join(map(str , result)))