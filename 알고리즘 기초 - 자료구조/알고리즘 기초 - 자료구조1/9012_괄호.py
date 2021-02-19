import sys

N = int(input())

lstack = 0
rstack = 0

for i in range(N) :
    ps = sys.stdin.readline()

    for j in ps :
        if j == '(' :
            lstack += 1
        elif j == ')' :
            if (lstack != 0) :
                lstack = lstack - 1
            else :
                rstack += 1

    if (lstack == 0) and (rstack == 0) :
        print('YES')
    else :
        print('NO')
        
    lstack = 0
    rstack = 0

