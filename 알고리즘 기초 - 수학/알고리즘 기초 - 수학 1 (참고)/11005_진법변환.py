Num , N = map(int , input().split())
result = ""
while Num != 0 :
    v = Num % N 
    Num = Num // N 
    if v >= 10 :
        result = chr(v+55) + result 
    else :
        result = str(v) + result
print(result)