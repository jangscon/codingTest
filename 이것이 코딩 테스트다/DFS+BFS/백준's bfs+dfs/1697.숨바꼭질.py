N , K = map(int , input().split(' '))

graph = [0 for _ in range(100000)]
def bfs() :
    from collections import deque
    queue = deque()
    queue.append(N)

    count = 1
    while queue :
        p = queue.popleft()
        graph[p] = count
        direction = [p+1 , p-1 , 2*p]
        for i in direction :
            if i > 0 :
                if graph[i] == 0 or (graph[i] != 0 and graph[i] > count) :
                    queue.append(i)

bfs()
print(graph[K])