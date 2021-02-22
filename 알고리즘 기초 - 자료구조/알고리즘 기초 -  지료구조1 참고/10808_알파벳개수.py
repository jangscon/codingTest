
S = list(input())

count = [0]*26

for word in S :
    count[ord(word) - 97] += 1

for i in count :
    print("{} ".format(i),end='')