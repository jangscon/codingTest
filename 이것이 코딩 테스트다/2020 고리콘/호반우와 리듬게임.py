n = int(input())
note = list(map(int , input().split()))
dp = [0 for _ in range(n)]
combo = 0
result = 0
count_fail = 0

while True :