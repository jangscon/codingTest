little_man = [int(input()) for _ in range(9)]
result = []
total = sum(little_man)

for i in range(9) :
    for j in range(i+1,9) :
        if total - (little_man[i] +little_man[j]) == 100 :
            remove_num = [little_man[i] , little_man[j]]
            little_man.remove(remove_num[0])
            little_man.remove(remove_num[1])
            little_man.sort()
            for k in little_man :
                print(k)
            break
    if len(little_man) == 7 :
        break

