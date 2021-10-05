from collections import deque

N , M = map(int , input().split() )
table = []
for i in range(N) :
    table.append(list(map(int, list(input()))))

def bfs(x , y) :

    queue = deque()
    queue.append((x,y))

    while queue :
        qx,qy = queue.popleft()
        move = [(qx+1 , qy), (qx-1 , qy), (qx , qy+1), (qx , qy-1)]

        # if qx == M-1 and qy == N-1 :
        #     break
        for i in move :

            if i[0] >= M or i[0] < 0 or i[1] >= N or i[1] < 0  :
                continue
            if table[i[1]][i[0]] == 0 :
                continue
            if table[i[1]][i[0]] == 1 :
                queue.append(i)
                table[i[1]][i[0]] = table[qy][qx] + 1



bfs(0,0)
print(table[N-1][M-1])







