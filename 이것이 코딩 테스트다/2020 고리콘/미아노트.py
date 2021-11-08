N , H , W = map(int , input().split())

encryp = []
plaintext = ""

for i in range(H) :
    encryp.append(input())

for i in range(0,N*W,W) :
    temp = ""
    for j in range(H) :
        temp += encryp[j][i:i+W]
    temp = list(set(temp))
    if len(temp) == 1 :
        plaintext += temp[0]
    else :
        plaintext += temp[0] if temp[0] != "?" else temp[1]

print(plaintext)

