N , K = map(int , input().split())
array_A = []
array_B = []
array_A.extend(list(map(int , input().split())))
array_B.extend(list(map(int , input().split())))
array_A.sort()
array_B.sort(reverse=True)

for i in range(K) :
    if array_A[i] < array_B[i] :
        array_A[i] = array_B[i]
    else :
        break
print(sum(array_A))