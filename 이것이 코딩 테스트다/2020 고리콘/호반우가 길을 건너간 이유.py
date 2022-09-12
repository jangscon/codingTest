from collections import deque

n , m = map(int , input().split())
farm = []
for _ in range(n) :
    farm.append(list(map(int , input().split())))
queue = deque()
def bfs():
    queue.append(farm[0][0])
