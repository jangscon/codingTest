A , P = map(int , input().split())

permutation = [A]
while True :
    sum = 0
    for i in str(permutation[-1]) :
        sum += int(i)**P
    if sum in permutation :
        break
    permutation.append(sum)

print(permutation.index(sum))