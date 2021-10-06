N = int(input())

for _ in range(N) :
    p_num = int(input())
    p = [''] + list(map(int ,input().split()))

    check = [False for _ in range(p_num+1)]
    cycle = 0
    for i in range(1, p_num+1) :
        if p[i] == i :
            check[i] = True
            cycle += 1
            continue
        current_spot = i
        check_cycle = False
        while True :
            if current_spot == i :
                if check[current_spot] :
                    break
                else :
                    check_cycle = True
            check[current_spot] = True
            current_spot = p[current_spot]
        if check_cycle :
            cycle += 1
    print(cycle)














