N , M = map(int , input().split())

List = [True]*(M+1)
List[1] = False
num = 2

for i in range(2 , M+1) :
    if List[i] == True :
        temp = i * 2 
        while temp <= M :
            List[temp] = False
            temp += i

for i in range(N,M+1) :
    if List[i] == True :
        print(i)
    
