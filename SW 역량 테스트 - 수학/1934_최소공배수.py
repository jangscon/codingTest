
n = int(input())
listLCM = []

def gcd(a , b) :
    while (b) :
        a , b = b , a%b
    return a

def lcm(a , b) :
    result = (a*b) // gcd(a,b)
    return result 


for i in range(0,n) :
    A ,B = input().split()
    listLCM.append(lcm(int(A),int(B)))

for i in listLCM :
    print(i)
