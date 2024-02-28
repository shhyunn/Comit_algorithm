import sys
from collections import deque
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N,M = map(int, input().split())
ladder = {}
snake = {}
board = [0]*101
visited = [False]*101

for _ in range(N):
    x,y = map(int,input().split())
    ladder[x] = y

for _ in range(M):
    u,v = map(int, input().split())
    snake[u] = v

q = deque([1])
while q:
    x = q.popleft()
    if x == 100:
        print(board[x])
        break

    for i in range(1,7):
        next = x + i
        if next <= 100 and not visited[next]:
            if next in ladder.keys():
                next = ladder[next]

            if next in snake.keys():
                next = snake[next]

            if not visited[next]:
                board[next] = board[x] + 1
                visited[next] = True
                q.append(next)
