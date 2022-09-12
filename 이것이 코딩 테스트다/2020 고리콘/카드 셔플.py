n = int(input())
test_case = []
for i in range(n) :
    test_case.append(list(map(int , input().split())))

for i in test_case :
    result = ""
    card = [j for j in range(i[0]+1)]
    A , B = i[1] , i[2]
    BisOdd = True if B % 2 == 1 else False
    while True :
        if A//2+1 and BisOdd :
            
