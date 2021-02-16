N = int(input())
primeNumCount = 0

def isPrime(num) :
    i = num-1
    if i == 0 :
        return False
    while i > 1 :
        if num % i == 0 :
            return False
        else :
            i -= 1
    return True

members = list(map(int , input().split()))
for i in range(0,N):
    primeNumCount += ( isPrime(members[i]) and 1 or 0 )
print(primeNumCount)