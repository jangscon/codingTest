spot = input()

row = int(spot[1])
column  = int(ord(spot[0])) - int(ord('a')) + 1

steps = [(1,2) , (1,-2) , (-1,2),(-1,-2) , (2,1),(2,-1),(-2,1),(-2,-1)]

count = 0

for step in steps :
    row_step = row + step[0]
    column_step = column + step[1]
    if row_step <= 8 and row_step > 0 and column_step > 0 and column_step <= 8 :
        print(step)
        count += 1

print(count)
