import sys
from collections import deque
import heapq

input = sys.stdin.readline

N,K = map(int, input().split())
visited = [False for _ in range(100001)]

stack = [(0,N)]
visited[N] = True

while stack:
    cnt, curr = heapq.heappop(stack)

    if curr == K:
        print(cnt)
        break
    else:
        next = [(cnt,2*curr),(cnt+1,curr+1),(cnt+1,curr-1)]
        
        for s in next:
            if 0 <= s[1] <= 100000 and not visited[s[1]]:
                heapq.heappush(stack,(s[0],s[1]))
                visited[s[1]] = True