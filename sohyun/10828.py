
import sys
input = sys.stdin.readline
N = int(input())
stack = []
d = len(stack)

for _ in range(N):
    strr = input()
    if strr.startswith("push"):
        _, num = strr.split()
        stack.append(int(num))
        d+=1
    
    elif strr.startswith("top"):
        if d > 0:
            print(stack[-1])
        else:
            print(-1)

    elif strr.startswith("size"):
        print(d)

    elif strr.startswith("empty"):
        if d == 0:
            print(1)
        else:
            print(0)

    elif strr.startswith("pop"):
        if d > 0:
            print(stack.pop())
            d -= 1
        else:
            print(-1)