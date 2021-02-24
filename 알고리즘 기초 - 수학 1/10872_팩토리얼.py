N = int(input())

if N == 0 :
    print(1)
else :
    result = 1
    while N != 0 :
        result *= N
        N -= 1
    print(result)
    