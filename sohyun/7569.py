import sys
from collections import deque
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
M,N,H = map(int, input().split())
tomato = [[] for _ in range(H)]
for i in range(H):
    for j in range(N):
        tomato[i].append(list(map(int, input().split())))

#bfs
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

#1: 익은 토마토, 0:익지 않은 토마토, -1:토마토가 들어있지 않음
start_x = -1
start_y = -1
start_z = -1
zero = 0
one = 0
stack = deque([])
for h in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[h][i][j] == 1:
                stack.append((h,i,j,0))
            elif tomato[h][i][j] == 0:
                zero += 1
               
if zero == 0:
    print(0)

else:
    max_cnt = 0
    while stack:
        z,y,x,cnt = stack.popleft()
        if cnt > max_cnt:
            max_cnt = cnt
        for i in range(6):
            cz = z + dz[i]
            cy = y + dy[i]
            cx = x + dx[i]

            if 0 <= cz < H and 0 <= cy < N and 0 <= cx < M:
                if tomato[cz][cy][cx] == 0:
                    stack.append((cz,cy,cx,cnt+1))
                    tomato[cz][cy][cx] = 1
                    zero -= 1
    if zero == 0:           
        print(max_cnt)
    else:
        print(-1)