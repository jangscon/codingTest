import sys

n = int(input())
part = sorted(list(map(int , sys.stdin.readline().split())))
m = int(input())
part_needed = sorted(list(map(int , sys.stdin.readline().split())))

def search_part(search_num) :
    left = 0
    right = n-1
    current_index = (left+right)//2
    while True :
        if left > right :
            return False
        if search_num == part[current_index] :
            return True
        elif search_num > part[current_index] :
            left = current_index + 1
            current_index = (left+right)//2
        elif search_num < part[current_index]:
            right = current_index -1
            current_index = (left + right) // 2
        elif current_index == 0 :
            return False

for i in range(m) :
    if search_part(part_needed[i]) :
        print("yes ",end='')
    else :
        print("no ", end='')