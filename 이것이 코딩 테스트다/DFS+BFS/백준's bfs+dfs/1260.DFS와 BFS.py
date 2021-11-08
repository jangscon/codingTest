from collections import deque


N , M , V = list(map(int , input().split()))
node = [[False for j in range(N)] for i in range(N)]

for i in range(M) :
    x, y = list(map(int , input().split()))
    node[x-1][y-1] = True
    node[y-1][x-1] = True


result = []
result2 = []
checkbox = [True for _ in range(N)]

def dfs(v) :
    checkbox[v] = False
    result.append(str(v + 1))
    for i in range(N) :
        if node[v][i] != False and checkbox[i]:
            dfs(i)


def bfs(v) :
    checkbox = [True for _ in range(N)]
    queue = deque()
    checkbox[v] = False
    queue.append(v)
    while queue :
        p = queue.popleft()
        result2.append(str(p+1))
        for i in range(N) :
            if checkbox[i] and node[p][i] != False:
                checkbox[i] = False
                queue.append(i)

bfs(V-1)
dfs(V-1)
print(' '.join(result))
print(' '.join(result2))