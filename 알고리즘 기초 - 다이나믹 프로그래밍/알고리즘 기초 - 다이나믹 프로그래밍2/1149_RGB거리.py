n = int(input())
RGB = [[0,0,0]]
for _ in range(n) :
    RGB.append( list(map( int,input().split())))

for i in range(1,n+1) :
    for j in range(3) :
        RGB[i][j] = min(RGB[i-1][(j+1)%3] , RGB[i-1][(j+2)%3]) + RGB[i][j]

# print(RGB)
print(min(RGB[n]))
