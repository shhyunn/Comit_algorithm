import sys
from collections import deque
input = sys.stdin.readline
A,B = map(int, input().split())
stack = deque([(A,1)])

find = 0
while stack:
    v,cnt = stack.popleft()
    if v == B:
        find = 1
        break
    n1 = v*2
    if n1 <= B:
        stack.append((n1,cnt+1))

    n2 = int(str(v)+"1")
    if n2 <= B:
        stack.append((n2,cnt+1))

if find == 1:
    print(cnt)
else:
    print(-1)