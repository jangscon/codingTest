

n = input().rstrip()
result = ""
stack = ""
iswrong = False
isww = False
num = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
for i in list(n) :
    stack += i
    if i == "x" :
        iswrong = True
        result += i
        stack = ""
    if stack in num :
        iswrong = False
        result += str(num.index(stack))
        if len(result) == 1 or not result[-2].isdigit() :
            isww = True
            break
        stack = ""
    if not i.isalpha() :
        if iswrong :
            isww = True
            break
        iswrong = True
        result += i
        stack = ""

temp = result
if not isww :
    result = str(eval(result[:-1].replace('x', '*').replace('/', '//')))
    result2 = ""
    for i in result:
        if i.isdigit():
            result2 += num[int(i)]
        else:
            result2 += i
    print(temp)
    print(result2)
else :
    print("Madness!")
