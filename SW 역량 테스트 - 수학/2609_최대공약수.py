inA, inB = input().split()
A = int(inA)
B = int(inB)

# 유클리드 호제법을 사용하여 해결
# a,b의 최대공약수를 찾는데 a = bq + r (0 <= r < b) 이라 하면 
# a,b의 최대공약수는 b,r의 최대공약수와 같다.
# 그래서 a와 b에 각각 b와 a%b(== (bq + r)%b == r)를 b가 0이 될때까지 하면 a는 최대공약수가 된다.
# 예를 들어 X = a*b , Y = b*c 이면
# 최대공약수는 b , 최소공배수는 a*b*c 이다.
# 최소공배수는 X,Y를 곱하고 최대공약수로 나누면 나온다.

def gcd(a , b) :
    while (b) :
        a , b = b , a%b
    return a

def lcm(a , b) :
    result = (a*b) // gcd(a,b)
    return result

print(gcd(A,B))
print(lcm(A,B))
