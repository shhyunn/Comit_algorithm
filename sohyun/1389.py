import sys
from collections import deque
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
#케빈베이컨 수가 가장 적은 사람 찾기, 그 친구들의 관계도 찾기
#1,N까지 사람 번호
N,M = map(int, input().split())
friends = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

def bfs(x):
    stack = deque([x])
    visited = [0 for _ in range(N+1)]
    visited[x] = 1
    res = [0 for _ in range(N+1)]

    while len(stack) != 0:
        a = stack.popleft()
        for i in friends[a]:
            if visited[i] == 0:
                res[i] = res[a] + 1
                visited[i] = 1
                stack.append(i)
    return sum(res)

ans = []
for i in range(1,N+1):
    ans.append(bfs(i))

print(ans.index(min(ans))+1)

