n , L = map(int , input().split())
center_list = list(map(int , input().split()))
center_sum = 0

isStable = True

for i in range(n-1,1,-1) :
    center_sum += center_list[i]

    if center_list[i-1] - L < center_sum / i < center_list[i-1] + L :
        isStable = True
    else :
        isStable = False
        break

if isStable :
    print("stable")
else :
    print("unstable")

