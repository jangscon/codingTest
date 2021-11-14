n = int(input())
tile = [0]*31
tile[0] = 1
tile[2] = 3

if n < 4 :
    print(tile[n])
else :
    for i in range(4 , n+1) :
        tile[i] = tile[i-2]*3
        for j in range(4, n+1 , 2) :
            tile[i] += tile[i-j]*2
    print(tile[n])