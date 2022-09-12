n = int(input())
a = [list(input()) for _ in range(n)]
result = 0
# 좌우 바꾸기
def find_long_candy(i,ii,j,jj) :
    global result
    a[ii][jj], a[i][j] = a[i][j], a[ii][jj]
    temp = [a[i][j], 0]
    for k in range(n):
        if temp[0] == a[k][jj]:
            temp[1] += 1
        else:
            result = temp[1] if temp[1] > result else result
            temp = [a[k][jj], 0]
    result = temp[1] if temp[1] > result else result

    for k in range(n):
        if temp[0] == a[k][j]:
            temp[1] += 1
        else:
            result = temp[1] if temp[1] > result else result
            temp = [a[k][j], 0]
    result = temp[1] if temp[1] > result else result
    a[i][j + 1], a[i][j] = a[i][j], a[i][j + 1]

for i in range(n) :
    for j in range(n-1) :
        find_long_candy(i,i+1,j,j)
        find_long_candy(j,j+1,i,i)
print(a)
print(result)