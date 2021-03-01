
Num , N = input().split()
N = int(N)
Num = Num[::-1]
result = 0

for i in range(len(Num)) :
    if Num[i].isdigit() :
        result += int(Num[i])*(N**i)
    elif Num[i].isalpha() :
        result += (ord(Num[i]) - 55)*(N**i)

print(result)
