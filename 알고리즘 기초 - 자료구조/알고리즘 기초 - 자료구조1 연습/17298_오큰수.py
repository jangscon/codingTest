from sys import stdin

# 시간초과때문에 상당히 어려웠다. 
# 한 블로그에서는 출력할 리스트를 -1로 초기화 해두고 거기서 조건이 되는 원소만 바꾸는 형식을 했다.
# 스택을 사용한 이유는 while문 탈출을 위한거 같다.
# 출처 : https://dirmathfl.tistory.com/68?category=825041

N  = int(input())
nums = list(map(int , stdin.readline().rstrip().split()))

stack = [0]
output = [-1]*N

i = 1

while i < N :
    while stack and nums[stack[-1]] < nums[i] :
        output[stack[-1]] = nums[i]
        stack.pop()

    stack.append(i)
    i += 1
for num in output :
    print(num,end=' ')