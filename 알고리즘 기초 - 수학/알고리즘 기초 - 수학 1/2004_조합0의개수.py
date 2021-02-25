n , m = map(int , input().split())

def dos_count(n) :
    result = 0
    while n != 0 :
        n = n // 2 
        result += n
    return result

def cinco_count(n) :
    result  = 0
    while n != 0 :
        n = n // 5 
        result += n
    return result

print(min(dos_count(n) - dos_count(m) - dos_count(n-m) , cinco_count(n) - cinco_count(m) - cinco_count(n-m)))