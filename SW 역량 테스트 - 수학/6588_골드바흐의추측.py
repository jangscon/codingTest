# t가 true면 소수숫자들 false면 소수인지 아닌지 표현한 진리값

def findPrimeNum_bool(n,t) :
    a = [False , False] + [True]*(n-1)
    prime = []
    for i in range(2 , n+1) :
        if a[i]:
            prime.append(i)
        for j in range(2*i, n+1 , i) : 
            a[j] = False
    return t and prime or a

prime_num = findPrimeNum_bool(1000000 , True)
prime_index = findPrimeNum_bool(1000000 , False)

goldbachList = []
while True : 
    N = int(input())
    if N == 0 :
        break

    for i in range(N // 2) :
        if prime_index[N-prime_num[i]] == True:
            goldbachList.append("{} = {} + {}".format(N, prime_num[i], N-prime_num[i]))
            break

for i in range(len(goldbachList)) :
    print(goldbachList[i])
    