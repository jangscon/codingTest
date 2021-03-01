A , B = map(int , input().split())
m = int(input())
listA = list(input().split())
listB = []
sum = 0

for i in range(len(listA)) :
    temp = listA.pop(-1)
    sum += int(temp)*(A**i)

while sum != 0 :
    temp = sum % B 
    sum = sum // B 
    listB.append(temp)

for i in listB[::-1] :
    print("{} ".format(i) ,end='')