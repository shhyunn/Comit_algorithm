#bfs와 dfs , 방문 정점이 여러개인 경우 정점 번호가 작은 것을 먼저 방문
import sys
from collections import deque
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N,M,V = map(int, input().split())
dic = {key:[] for key in range(1,N+1)}

# def dfs(N,V):
#     visited = [0 for _ in range(N)]
#     stack = deque([V])
#     while stack:
#         v = stack.popleft()
#         if not visited[v-1]:
#             # stack = dic[v] + stack
#             for k in dic[v]:
#                 stack.appendleft(k)
#             visited[v-1] = 1
#             print(v, end=" ")
def _dfs(v,visited):
    visited[v-1] = 1
    print(v, end=" ")
    for i in dic[v]:
        if not visited[i-1]:
            _dfs(i,visited)
    
def dfs(N,V):
    visited = [0 for _ in range(N)]
    _dfs(V,visited)

def bfs(N,V):
    visited = [0 for _ in range(N)]
    stack = deque([V])
    visited[V-1] = 1
    while stack:
        v = stack.popleft()
        print(v, end=" ")

        for k in dic[v]:
            if not visited[k-1]:
                stack.append(k)
                visited[k-1] = 1           

for _ in range(M):
    t,w = map(int, input().split())
    dic[t].append(w)
    dic[w].append(t)

for i in dic.keys():
    dic[i].sort()

dfs(N,V)
print()
bfs(N,V)     

