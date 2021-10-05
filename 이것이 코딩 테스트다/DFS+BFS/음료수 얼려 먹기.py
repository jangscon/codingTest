N , M = map(int , input().split())
table = []

for i in range(N) :
    table.append(list(map(int , list(input()))))

result = 0

def dfs(x , y) :

    if  x >= M or x < 0 or y >= N or y < 0 :
        return False
    
    if table[y][x] == 0 :
        table[y][x] = 1
        dfs(x + 1 , y)
        dfs(x - 1 , y)
        dfs(x , y + 1)
        dfs(x , y - 1)
        return True
    return False


for i in range(N) :
    for j in range(M) :
        if dfs(j,i) == True :
            result += 1

print(result)



