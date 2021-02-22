while True :
    try:
        S = list(input())
    except:
        break
    up , sm , num , sp = 0,0,0,0
    for word in S :
        if word.isupper() :   up += 1
        elif word.islower() : sm += 1
        elif word.isdigit() : num += 1
        elif word.isspace() : sp += 1
    print(sm,up,num,sp)
