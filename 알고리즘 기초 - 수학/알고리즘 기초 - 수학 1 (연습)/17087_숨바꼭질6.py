from math import gcd

N , S = map(int , input().split())
siblings = list(map(int , input().split()))

first = siblings.pop(0)
result = first > S and first - S or S - first

if siblings :
    for i in siblings :
        current = i > S and i - S or S - i    
        result = gcd(result , current)

print(result)
