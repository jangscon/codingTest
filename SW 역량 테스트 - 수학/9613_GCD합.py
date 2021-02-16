n = int(input())

def gcd(a , b) :
    while(b) :
        a, b = b,a%b
    return a


def comb(array, r):
    for i in range(len(array)):
        if r == 1: 
            yield [array[i]]
        else:
            for next in comb(array[i+1:], r-1):
                yield [array[i]] + next


comList = []
for i in range(0 , n) :
    inputm = list(input().partition(' '))
    m =  int(inputm[0])
    members = list(map(int , inputm[2].split()))
    comsum = 0
    for j in comb(members, 2):
        comsum += gcd(j[0],j[1])
    comList.append(comsum)

for i in range(0,len(comList)) :
    print(comList[i])