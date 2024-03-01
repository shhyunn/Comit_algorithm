import sys
from collections import deque

sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N = int(input())
res = [-1 for _ in range(N+1)]
graph = {key:[] for key in range(1,N+1)}
visited = [False for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = deque([1])
visited[1] = True
while stack:
    v = stack.popleft()
    for i in graph[v]:
        if not visited[i]:
            stack.append(i)
            visited[i] = True
            res[i] = v

for r in range(2,N+1):
    print(res[r])
