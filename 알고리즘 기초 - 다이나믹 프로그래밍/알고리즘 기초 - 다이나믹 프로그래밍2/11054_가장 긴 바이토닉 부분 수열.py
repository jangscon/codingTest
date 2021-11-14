n = int(input())
nums = [0]+list(map(int, input().split()))
left = [0]*(n+1)
right = [0]*(n+1)


for i in range(1 , n+1) :
    left[i] = 1
    right[n-i+1] = 1
    for j in range(1 , i) :
        if nums[j] < nums[i] and left[j]+1 > left[i] :
            left[i] = left[j]+1
        if nums[n-i+1] > nums[n-j+1] and right[n-i+1] < right[n-j+1]+1 :
            right[n-i+1] = right[n-j+1]+1

print(left)
print(right)
print(max(map((lambda x, y : x+y), left,right))-1)


