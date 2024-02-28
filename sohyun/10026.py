import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

N = int(input())
color = []
for _ in range(N):
    color.append(list(input().strip()))
visited = [[0 for _ in range(N)] for _ in range(N)]
normal = 0
special = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            stack = [(i,j)]
            visited[i][j] = 1
            while stack:
                x,y = stack.pop()

                for k in range(4):
                    cx = x + dx[k]
                    cy = y + dy[k]
                    if 0 <= cx < N and 0 <= cy < N:
                        if color[cx][cy] == color[x][y] and visited[cx][cy] == 0:
                            stack.append((cx,cy))
                            visited[cx][cy] = 1
            normal += 1

visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            stack = [(i,j)]
            visited[i][j] = 1
            while stack:
                x,y = stack.pop()
                for k in range(4):
                    cx = x + dx[k]
                    cy = y + dy[k]
                    if 0 <= cx < N and 0 <= cy < N and visited[cx][cy] == 0:
                        if color[x][y] == "B":
                            if color[cx][cy] == color[x][y]:
                                stack.append((cx,cy))
                                visited[cx][cy] = 1
                        else:
                            if color[cx][cy] !="B":
                                stack.append((cx,cy))
                                visited[cx][cy] = 1
                                

            special += 1

print(normal,special)