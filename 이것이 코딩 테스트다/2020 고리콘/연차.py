start = list(map(int , input().split()))
end = list(map(int , input().split()))

s =   start[1]*30 + start[2]
e =  (end[0] - start[0])*360 + end[1]*30 + end[2]

day = e-s
year = day // 360
if year != 0 :
    if year % 2 == 1 :
        year += 1
    temp = year-1
    year = year*15 + (year//2-1)*(year//2)
    if (day // 360) % 2 == 1 :
        year -= (15 + temp//2)

month = day // 30 if day // 30 <= 36 else 36
print(str(year) + " " + str(month))
print(str(day)+"days")