from collections import deque
import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
def bfs(s):
    q = deque()
    visited = [0 for _ in range(n+1)]

    q.append(s)
    visited[s] = 1

    while q:
        x = q.popleft()

        for i in tree[x]:
            if visited[i] == 0:
                visited[i] = 1
                result[i] = result[x] + 1
                q.append(i)


n = int(input())
a, b = map(int, input().split())
m = int(input())
tree = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    tree[x].append(y)#모두 저장
    tree[y].append(x)

bfs(a) #a 기준으로 bfs 진행
if result[b] != 0: 
    print(result[b])
else:
    print(-1)

# import sys
# from collections import deque
# sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
# input = sys.stdin.readline

# n = int(input())
# a,b = map(int, input().split())
# m = int(input())
# dic = {key:[] for key in range(n+1)}
# visited = [0 for _ in range(n+1)]
# classes = [0 for _ in range(n+1)]

# for _ in range(m):
#     i,j = map(int, input().split())
#     dic[i].append(j)

# cnt = 0
# for k in range(1,n+1):
#     if not visited[k]:
#         cnt += 1
#         stack = deque([k])
#         visited[k] = 1
#         classes[k] = cnt
#         while stack:
#             q = stack.popleft()
#             cnt += 1
#             print(q)
#             for j in dic[q]:
#                 if not visited[j]:
#                     stack.append(j)
#                     visited[j] = 1
#                     classes[j] = cnt
# print(classes)
