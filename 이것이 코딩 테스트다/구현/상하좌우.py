n = int(input())
plans = input().split()
x = 1
y = 1

for i in plans :
    if i == 'R' :
        if x < n : x += 1
    elif i == 'L' :
        if x > 1 : x -= 1
    elif i == 'U' :
        if y > 1 : y -= 1
    elif i == 'D' :
        if y < n : y += 1

print(y , x)