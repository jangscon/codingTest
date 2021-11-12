n,m = map(int , input().split())
ricecakes = sorted(list(map(int , input().split())),reverse=True)

def search_suitable_len() :
    left = 0
    right = ricecakes[0]
    mid = (left + right) // 2
    temp_mid = mid
    while True :
        if left > right :
            return temp_mid
        ricesum = sum(map(lambda x : x - mid , filter(lambda x : x > mid , ricecakes)))
        if ricesum == m :
            return mid
        elif ricesum > m :
            left = mid + 1
            temp_mid = mid
            mid = (left + right) // 2
        elif ricesum < m :
            right = mid - 1
            temp_mid = mid
            mid = (left + right) // 2

print(search_suitable_len())