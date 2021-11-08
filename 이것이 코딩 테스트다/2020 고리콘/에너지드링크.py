N = int(input())
drinks = list(map(int , input().split()))
drinks.sort(reverse=True)

total_drinks = drinks[0]
for i in range(1,N) :
    total_drinks += drinks[i]/2

print(total_drinks)
