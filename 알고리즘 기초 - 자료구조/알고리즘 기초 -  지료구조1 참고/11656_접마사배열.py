# 파이썬에서는 엄청 쉬운 문제 sorted 하나로 해결 가능하다는게 놀랍다 

N = list(input())

suffix = []

for i in range(len(N)) :
    suffix.append(N[i:])

result = sorted(suffix) 

for i in result :
    print(''.join(i))