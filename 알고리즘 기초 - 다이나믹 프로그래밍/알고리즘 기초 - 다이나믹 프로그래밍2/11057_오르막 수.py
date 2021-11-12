n = int(input())
nums = [1 for i in range(10)]

for i in range(1,n) :
    temp = []
    for j in range(10) :
        temp.append(sum(nums[:j+1]))
    nums = temp

print(sum(nums)%10007)

