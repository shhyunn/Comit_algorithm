import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int, input().split())
#N,K 걸을 때 X-1 OR X+1 OR 2*X -> 찾을 수 있는 가장 빠른 시간은? 카운팅?
# A = min(N,K)
# B = max(N,K)
visited = [0]*100001
#BFS
def bfs(a,b):
    cnt = 0
    stack = deque([(a,cnt)])
    visited[a] = 1
    while stack:
        k,cnt = stack.popleft()
        if k == b:
            return cnt
        
        lst = [k-1,k+1,k*2]
        for n in lst:
            if 0 <= n <= 100000 and visited[n] == 0:
                stack.append((n,cnt+1))
                visited[n] = 1

print(bfs(N,K))