n = int(input())
mtrx = []
for i in range(n) :
    mtrx.append(input())

issator = True

for i in range(n) :
    for j in range(i+1) :
        if mtrx[i][j] != mtrx[j][i] :
            issator = False
            break
    if not issator :
        break

if issator :
    print("YES")
else :
    print("NO")


