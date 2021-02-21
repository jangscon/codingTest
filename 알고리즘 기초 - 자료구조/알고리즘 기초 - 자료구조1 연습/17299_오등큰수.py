from sys import stdin
from collections import Counter


stack = []
n = int(stdin.readline())
s = list(stdin.readline().split())
cnt = Counter(s)

# s는 n * 2 배열로 s[num][1]은 기존의 입력값이고 s[num][0]은 입력값의 빈도이다. 
s = [[cnt[num], int(num)] for num in s]

answer = [-1 for _ in range(n)]
stack.append(0)
i = 1

while stack and i < n:
    while stack and s[stack[-1]][0] < s[i][0]:
        answer[stack[-1]] = s[i][1]
        stack.pop()
    stack.append(i)
    i += 1
for num in answer:
    print(num, end=' ')