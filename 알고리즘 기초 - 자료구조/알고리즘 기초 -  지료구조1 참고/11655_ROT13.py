N = list(input())

for i in range(len(N)) :
    word = N[i]
    if word.islower() :
        if ord(word) + 13 > 122 :
            N[i] = chr(ord(word) - 13)
        else : N[i] = chr(ord(word) + 13)
    elif word.isupper() :
        if ord(word) + 13 > 90 :
            N[i] = chr(ord(word) - 13)
        else : N[i] = chr(ord(word) + 13)

print(''.join(N))