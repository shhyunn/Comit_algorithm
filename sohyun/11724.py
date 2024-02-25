import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

N,M = map(int, input().split())
visited = [0]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1,N+1):
    if visited[i] == 1:
        continue
    stack = [i]
    visited[i] = 1
    while stack != []:
        k = stack.pop()
        for j in graph[k]:
            if visited[j] == 1:
                continue
            stack.append(j)
            visited[j] = 1
    cnt += 1

print(cnt)

