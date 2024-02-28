import sys
from collections import deque
input = sys.stdin.readline

S = int(input())
visited = [[False for _ in range(S+1)] for _ in range(S+1)]
stack = deque([(1,0,0)])
visited[1][0] = True
while stack:
    x,cnt,clip = stack.popleft()
    if x == S:
        print(cnt)
        break
    
    if clip != 0 and 0 <= x+clip <= S and not visited[x+clip][clip]:
        stack.append((x+clip,cnt+1,clip))
        visited[x+clip][clip] = True

    if not visited[x][x]:
        stack.append((x,cnt+1,x))
        visited[x][x] = True

    if 0 <= x-1 <= S and not visited[x-1][clip]:
        stack.append((x-1,cnt+1,clip))
        visited[x-1][clip] = True