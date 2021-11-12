# n = int(input())
# nums = [0] + list(map(int , input().split()))
# DP = [0 for _ in range(n+1)]
#
# def find_max() :
#     temp = nums[1:]
#     if max(temp) <= 0:
#         return max(temp)
#
#     DP[1] = nums[1]
#     for i in range(2,n+1) :
#         # print(DP)
#         DP[i] = max(DP[i-1] + nums[i] , DP[i])
#     return max(DP)
#
# print(find_max())

import math
print(math.sqrt(4) )