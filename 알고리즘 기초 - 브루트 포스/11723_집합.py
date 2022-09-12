from sys import stdin
m = int(stdin.readline())
num_set = set()

for _ in range(m) :
    cmd = stdin.readline().strip().split()
    if len(cmd) == 1:
        if cmd[0] == "all" :
            num_set = set([i for i in range(1, 21)])
        else :
            num_set = set()
    else :
        num , command = int(cmd[1]) , cmd[0]
        if command == "add" :
            num_set.add(num)
        elif command == "remove" :
            num_set.discard(num)
        elif command == "check" :
            print(1 if num in num_set else 0)
        elif command == "toggle" :
            num_set.discard(num) if num in num_set else num_set.add(num)
