import sys
from collections import deque
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

#며칠이 지나면 토마토가 다 익게 되는가?
M,N = map(int, input().split())
#m : 가로칸 수(열), n(행)
#1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토 없음
#모두 익지 못하는 상황이면 -1 출력, 모든 토마토가 익어있는 상황이면 0
tomato = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
stack = deque([])
empty = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            stack.append((i,j,0))
            visited[i][j] = 1
        elif tomato[i][j] == -1:
            empty += 1

ee = len(stack)
if ee == N*M-empty:
    print(0)
else:
    max_value = -1

    while len(stack) != 0:
        a,b,cnt = stack.popleft()

        if ee == N*M-empty:
            max_value = max(max_value, cnt)

        for i in range(4):
            cx = a + dx[i]
            cy = b + dy[i]
           
            if 0 <= cx < N and 0 <= cy < M and visited[cx][cy] == 0 and tomato[cx][cy] == 0:
                visited[cx][cy] = 1
                tomato[cx][cy] = 1
                ee += 1
                stack.append((cx,cy,cnt+1))
        
    print(max_value)