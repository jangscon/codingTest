num = int(input())

result = ""
temp = num


while temp != 1 and num != 0: 
    if temp % 2 == 0 :
        temp = temp // -2
        result = "0" + result
    else :
        temp = (temp-1) // -2
        result = "1" + result        

result = num == 0 and "0" or "1" + result

print(result)