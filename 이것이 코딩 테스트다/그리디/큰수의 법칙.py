
n , m , k = map(int ,input().split())
nums = list(map(int , input().split()))
nums.sort()

first = nums[n-1]
second = nums[n-2]

# n은 nums 길이 , m =  총 깅이 , k = 반복될 길이
# 가장 큰  수의 count는 m을 (k+1) 만큼 나눈 값과 그 나머지이다

count = int(m / (k+1)) * k
count += m % (k+1)

result = count * first + (m - count ) * second

print(result)






# result = 0
# while True :
#     if first == second :
#         result = first * m
#         break
#
#     for i in range(k) :
#         if m == 0 :
#             break
#         result += first
#         m -= 1
#
#     if m == 0:
#         break
#     result += second
#     m -= 1
#
# print(result)






