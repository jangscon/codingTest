e , s , m = map(int , input().split())
# e = 15 ,s = 28 , m = 19

days = 0
E , S , M  = 0,0,0
while True :
    days += 1
    E = (E + 1) % 16 if (E + 1) % 16 != 0 else 1
    S = (S + 1) % 29 if (S + 1) % 29 != 0 else 1
    M = (M + 1) % 20 if (M + 1) % 20 != 0 else 1
    if e == E and s == S and m == M :
        break
print(days)