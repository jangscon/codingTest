n , m = map(int , input().split())
paper = [list(map(int , input().split())) for _ in range(n)]
#
# 테트로미노 모양
#
#  0   0    00
#  0   00   00  000  0000
#  00   0        0
#

# 1번 : n/m , n+1/m , n+2/m , n+2/m+1  and  n/m , n/m+1 , n/m+2 ,n+
#

