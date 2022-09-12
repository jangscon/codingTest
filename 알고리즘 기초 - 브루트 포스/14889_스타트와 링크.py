from itertools import combinations

n = int(input())
startlink = []
indexlist = [i for i in range(n)]
result = 199
compare = 0
for i in range(n) :
    startlink.append(list(map(int, input().split())))

comb = list(combinations(indexlist , n//2))
for i in comb :
    compare = 0
    if len(i) > 2 :
        comb_bin = list(combinations(i , 2))
        for j in comb_bin :
            compare += (startlink[j[0]][j[1]] + startlink[j[1]][j[0]])
    else :
        compare += (startlink[i[0]][i[1]] + startlink[i[1]][i[0]])

    another = list(set(indexlist) - set(i))
    if len(another) > 2 :
        comb_bin = list(combinations(another , 2))
        for j in comb_bin :
            compare -= (startlink[j[0]][j[1]] + startlink[j[1]][j[0]])
    else :
        compare -= (startlink[another[0]][another[1]] + startlink[another[1]][another[0]])

    result = abs(compare) if abs(compare) < result else result

print(result)