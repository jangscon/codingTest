
binary = list(input())
binary.reverse()

result = ''

count = 0
add = 0
for i in binary :
    if i == '1' :
        add += pow(2,count)
    if count == 2 :
        result = str(add) + result
        add = 0
        count = 0
    else :
        count += 1
if count != 0 :
    result = str(add) + result

print(result) 