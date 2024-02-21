import sys
from collections import deque
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
N = int(input())
#bfs, 각 단지에 속하는 집의 수를 오름차순으로 정렬
gr = []
for _ in range(N):
    gr.append([int(i) for i in input()])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    res = []
    for x in range(N):
        for y in range(N):
            if gr[x][y] == 1:
                cnt = 1
                stack = deque([(x,y)])
                gr[x][y] = 0
                while stack:
                    a,b = stack.popleft()
                    for i in range(4):
                        cx = a + dx[i]
                        cy = b + dy[i]
                        if 0 <= cx < N and 0 <= cy < N and gr[cx][cy] == 1:
                            stack.append((cx,cy))
                            gr[cx][cy] = 0
                            cnt += 1

                res.append(cnt)
    return res

res_lst = bfs()
print(len(res_lst))
for id in sorted(res_lst):
    print(id)