import sys
from collections import deque
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

def bfs(start,find): #시작에서 찾을 거리까지 찾아보기
    queue = deque()
    queue.append((start,0)) #start넣기
    visited = [False]*(N+1) #방문했는지 확인
    visited[start] = True

    while queue:
        v,d = queue.popleft() #큐에서 하나 제거, bfs
        if v == find: #만약 찾는 것이라면 d 반환
            return d
        for i,l in dist[v]:
            if not visited[i]:
                visited[i] = True
                queue.append((i,d+l))


N,M = map(int,input().split())
dist = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,d = map(int, input().split())
    dist[a].append((b,d)) #거리와 함께 튜플 형태로 기록
    dist[b].append((a,d))

for _ in range(M):
    n1,n2 = map(int,input().split())
    print(bfs(n1,n2)) #내가 찾을 것을 bfs로..



