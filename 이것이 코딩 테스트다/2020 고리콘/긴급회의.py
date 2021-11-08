n = int(input())
vote_result = map(int, input().split())

result = [0 for i in range(n+1)]
most_top = [0]

for i in vote_result :
    if i == 0 :
        continue
    result[i] += 1
    if most_top[0] < result[i] :
        most_top[0] = result[i]
        del most_top[1:]
        most_top.append(i)
    elif most_top[0] == result[i] :
        most_top.append(i)

if len(most_top) > 2 :
    print("skipped")

else :
    print(most_top[1])
