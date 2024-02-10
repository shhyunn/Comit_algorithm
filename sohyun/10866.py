import sys
from collections import deque
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

N = int(input())
arr = deque([])
d = 0
for _ in range(N):
    strr = input()
    if strr.startswith("push_front"):
        _,n = strr.split()
        arr.appendleft(n)
        d += 1

    elif strr.startswith("push_back"):
        _,n = strr.split()
        arr.append(n)
        d += 1

    elif strr.startswith("pop_front"):
        if d == 0:
            print(-1)
        else:
            print(arr.popleft())
            d -= 1

    elif strr.startswith("pop_back"):
        if d == 0:
            print(-1)
        else:
            print(arr.pop()) 
            d -= 1

    elif strr.startswith("size"):
        print(d)
    
    elif strr.startswith("empty"):
        if d == 0:
            print(1)
        else:
            print(0)
    
    elif strr.startswith("front"):
        if d == 0:
            print(-1)
        else:
            print(arr[0])
    
    elif strr.startswith("back"):
        if d == 0:
            print(-1)
        else:
            print(arr[-1])