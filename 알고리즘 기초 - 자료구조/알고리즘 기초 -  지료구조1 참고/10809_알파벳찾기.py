S = list(input())

F = [-1]*26

for word in S :
    order = ord(word) - 97
    if F[order] == -1 :
        F[order] = S.index(word) 

for i in F :
    print("{} ".format(i),end='')