from sys import stdin 

N = int(input())
Deque = []

for i in range(N) :
    command = list(stdin.readline().split())
    if command[0] == 'push_front' :
        Deque.insert(0 , int(command[1]))
        continue
    elif command[0] == 'push_back' :
        Deque.append(int(command[1]))
        continue
    elif command[0] == 'pop_front' :
        if not Deque : print("-1")
        else : print(Deque.pop(0))
        continue
    elif command[0] == 'pop_back' :
        if not Deque : print('-1')
        else : print(Deque.pop(len(Deque)-1))
        continue
    elif command[0] == 'size' :
        if not Deque : print("0")
        else : print(len(Deque))
        continue
    elif command[0] == 'empty' :
        if not Deque : print("1")
        else : print("0")
        continue
    elif command[0] == 'front' :
        if not Deque : print('-1')
        else : print(Deque[0])
        continue
    elif command[0] == 'back' :
        if not Deque : print('-1')
        else : print(Deque[len(Deque) - 1])
        continue


