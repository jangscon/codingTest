import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N , M = map(int , input().split(' '))

graph = defaultdict(list)
check = []

for _ in range(M) :
    a , b = list(map(int , input().split(' ')))
    graph[a].append(b)
    graph[b].append(a)


def dfs(i) :
    if i in check :
        return False
    check.append(i)
    for j in graph[i] :
        dfs(j)
    return True

result = 0

for i in range(1,N+1) :
    if dfs(i) == True :
        result += 1
print(type(graph))
print(type(graph[1]))
print(graph[1])
print(result)