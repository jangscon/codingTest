from collections import deque

N , M = map(int , input().split())
table = [[-1 for _ in range(M)] for _ in range(N)]

for i in range(N) :
    temp = list(map(int , list(input())))
    for j in range(M) :
        if temp[j] == 1 :
            table[i][j] = 0


def find_shortest_path() :
    queue = deque()

    start = (0,0)
    queue.append(start)
    table[0][0] += 1

    while queue :
        x, y = queue.popleft()
        d = [(x+1 , y) ,(x-1 , y) ,(x, y+1) ,(x, y-1) ]
        for i in d :
            if i[0] >= M or i[0] < 0 or i[1] >= N or i[1] < 0 :
                continue
            if table[i[1]][i[0]] == -1 :
                continue
            if table[y][x] + 1 < table[i[1]][i[0]] or table[i[1]][i[0]] == 0:
                queue.append((i[0], i[1]))
                table[i[1]][i[0]] = table[y][x] + 1


find_shortest_path()
print(table[N-1][M-1])




