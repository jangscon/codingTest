N = int(input())

for _ in range(N) :
    p_num = int(input())
    p = list(input().split())

    cycle = 0
    pocket = []

    for i in range(p_num) :
        if i+1 == p[i] :
            cycle += 1
        else :
            pocket.append([i+1 , p[i]])











