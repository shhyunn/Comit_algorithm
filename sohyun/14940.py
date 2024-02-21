import sys
from collections import deque
#가로 및 세로로만 움직임
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
n,m = map(int, input().split())
maps = []
res = [[0 for _ in range(m)] for _ in range(n)] #결과값 저장
visited = [[0 for _ in range(m)] for _ in range(n)] #방문 여부

for _ in range(n):
    #0:못감, 1:갈수 있음, 2:목표지점, 2는 단 한개
    #각 지점에서 목표지점까지의 거리
    maps.append(list(map(int, input().split())))

res1 = 0
res2 = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 2: #시작지점 선정
            res1 = i
            res2 = j
            break

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    stack = deque([(x,y)]) #시작지점 queue에 넣기

    visited[x][y] = 1 #방문으로 표시
    while stack:#stack에 좌표가 있을 때까지 반복
        a,b = stack.popleft()
        for i in range(4): #4개 방향 점검
            cx = a + dx[i]
            cy = b + dy[i]
            if 0 <= cx < n and 0 <= cy < m and visited[cx][cy] == 0: #방문한 적이 없을 경우
                if maps[cx][cy] == 0: #갈 수 없는 땅인 경우
                    continue
               
                stack.append((cx,cy)) #추가
                res[cx][cy] = res[a][b]+1#현재 결과값에 +1
                visited[cx][cy] = 1 #방문으로 변경
        # curr += 1

bfs(res1,res2)
for i in range(n):
    for j in range(m):
        #갈 수 있는 땅인데, 도달 불가능인 경우
        if maps[i][j] == 1 and res[i][j] == 0:
            res[i][j] = -1

for ls in res:
    print(" ".join(map(str,ls)))
