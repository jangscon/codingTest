from copy import deepcopy

def dfs(table , x,y , depth) :
    if x < 0 or y < 0 or x >= N or y >= N :
        return False
    if table[y][x] <= depth :
        return False
    if table[y][x] != 0 :
        table[y][x] = 0
        dfs(table, x + 1 , y , depth)
        dfs(table, x - 1 , y , depth)
        dfs(table, x , y + 1 , depth)
        dfs(table, x , y - 1 , depth)
        return True
    return False

def bfs(table , x , y , depth) :
    if x < 0 or y < 0 or x >= N or y >= N :
        return False
    if table[y][x] <= depth :
        return False

    from collections import deque
    queue = deque()
    queue.append((x,y))

    while queue :
        i = queue.popleft()
        direction = [(i[0] + 1 , i[1]),(i[0] - 1 , i[1]),(i[0] , i[1] + 1),(i[0] , i[1] - 1)]
        for d in direction :
            if d[0] < 0 or d[1] < 0 or d[0] >= N or d[1] >= N or table[d[1]][d[0]] <= depth :
                continue
            if table[d[1]][d[0]] > depth :
                queue.append(d)
                table[d[1]][d[0]] = 0
    return True

N = int(input())

table = []

for _ in range(N) :
    table.append(list(map(int , input().split(' '))))

min_num = min(map(min , table))
max_num = max(map(max , table))
if min_num == max_num :
    min_num -= 1

result = 0
for n in range(min_num , max_num,1) :
    count = 0
    temp_table = deepcopy(table)
    for y in range(N) :
        for x in range(N) :
            if bfs(temp_table , x , y , n) == True :
                count += 1
    if result < count :
        result = count

print(result)

