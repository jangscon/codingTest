def turn_left(direction) :
    return direction - 1 if direction-1 > 0 else 3


N , M = map(int , input().split())
start = list(map(int,input().split()))

x = start[0]
y = start[1]
direction = start[2]

tmap = []
check = [[0] * M for _ in range(N)]
count = 1
turn_count = 0

for i in range(N) :
    tmap.append(list(map(int,input().split())))

tmap[x][y] = 1

while True :
    print(x, y , direction)
    if turn_count == 4 :
        break
    if direction == 0:
        if x - 1 >= 0 and check[x - 1][y] == 0 and tmap[x - 1][y] == 0:
            x = x - 1
            count += 1
            turn_count = 0
            check[x][y] = 1
        direction = turn_left(direction)
        turn_count += 1

    elif direction == 1:
        if y - 1 >= 0 and check[x][y - 1] == 0 and tmap[x][y - 1] == 0:
            y = y - 1
            count += 1
            turn_count = 0
            check[x][y] = 1
        direction = turn_left(direction)
        turn_count += 1

    elif direction == 2:
        if x + 1 < M and check[x + 1][y] == 0 and tmap[x + 1][y] == 0:
            x = x + 1
            count += 1
            turn_count = 0
            check[x][y] = 1
        direction = turn_left(direction)
        turn_count += 1

    else:
        if y + 1 < M and check[x][y + 1] == 0 and tmap[x][y + 1] == 0:
            y = y + 1
            count += 1
            turn_count = 0
            check[x][y] = 1
        direction = turn_left(direction)
        turn_count += 1


print(count)
