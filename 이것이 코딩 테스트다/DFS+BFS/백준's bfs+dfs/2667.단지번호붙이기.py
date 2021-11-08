
def dfs(table , x,y , depth) :
    if x < 0 or y < 0 or x >= N or y >= N :
        return False
    if table[y][x] == 0 :
        dfs(table, x + 1 , y , depth)
        dfs(table, x - 1 , y , depth)
        dfs(table, x , y + 1 , depth)
        dfs(table, x , y - 1 , depth)
        return True
    return False

N = int(input())

table = []

for _ in range(N) :
    table.append(list(map(int , list(input()))))

print("222222")

print(table)

min_num = min(map(min , table))
max_num = max(map(max , table))

result = 0

for n in range(min_num , max_num+1) :
    count = 0
    temp_table = table[:]
    print(temp_table)
    for y in range(N) :
        for x in range(N) :
            if dfs(temp_table , x , y , n) == True :
                count += 1
    if result < count :
        result = count

print(result)



