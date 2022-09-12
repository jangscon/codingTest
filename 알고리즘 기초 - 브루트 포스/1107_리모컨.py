N = int(input())
M = int(input())
button = {str(i) for i in range(0,10)}

if M != 0 :
    button = button - set(map(str , input().split()))

current = 100

# 우선 + , 로만 이동했을때 버튼 누르는 횟수
cnt = abs(N-current)

# 숫자로 이동했을때 버튼 누르는 횟수
for i in range(1000000) :
    for j in range(len(str(i))) :
        if str(i)[j] not in button :
            break
        elif j == len(str(i))-1 :
            cnt = min(cnt , len(str(i)) + abs(N - i))
print(cnt)