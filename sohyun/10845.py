import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    command = list(input().split())
    n = len(queue)

    if command[0] == "push":
        queue.append(int(command[1]))
        n += 1

    elif command[0] == "pop":
        if n == 0:
            print(-1)
        else:
            print(queue.pop(0))
            n -= 1

    elif command[0] == "size":
        print(n)
    
    elif command[0] == "empty":
        if n == 0:
            print(1)
        else:
            print(0)
            
    elif command[0] == "front":
        if n == 0:
            print(-1)
        else:
            print(queue[0])
    
    elif command[0] == "back":
        if n == 0:
            print(-1)
        else:
            print(queue[-1])