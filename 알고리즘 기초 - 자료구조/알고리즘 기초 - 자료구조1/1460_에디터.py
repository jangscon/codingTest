from sys import stdin 

# 커서를 따로 변수로 지정하여 처음에 시작하였는데 
# 이는 시간초과로 실패하고 인터넷을 찾아본 결과 너무 좋은 해답이 있었다.
# 두개의 스택을 커서 앞의 데이터와 커서 이후의 데이터들로 나눠서 서로 push pop해주면 
# 아주 간단하게 구현이 가능했다. 
# 구현해야할 것은 리스트(스택) 두개와 입력값들만 받아와 주면 끝이다!

string = list(stdin.readline().rstrip())
outString = []

n = int(input())
for _ in range(n) :
    sign = list(stdin.readline().rstrip())
    if sign[0] == 'L' :
        if string : outString.append(string.pop())
        else : continue
    elif sign[0] == 'D' :
        if outString : string.append(outString.pop())
        else : continue
    elif sign[0] == 'B' :
        if string : string.pop()
        else : continue
    elif sign[0] == 'P' :
        string.append(sign[2])

print(''.join(string + list(reversed(outString))))

