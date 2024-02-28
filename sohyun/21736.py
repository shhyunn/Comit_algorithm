import sys
from collections import deque
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

#캠퍼스 크기 NxM, 상하좌우로 이동, 만날 수 있는 사람의 수 출력
N,M = map(int, input().split())
campus = []
for _ in range(N):
    campus.append(list(input().strip()))

i1 = -1
i2 = -1
for i in range(N): #3
    for j in range(M):#5
        if campus[i][j] == "I":
            i1 = i
            i2 = j
            break

stack = deque([(i1,i2)])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
while len(stack) != 0:
    a,b = stack.popleft()
    for i in range(4):
        cx = a + dx[i]
        cy = b + dy[i]

        if 0 <= cx < N and 0 <= cy < M and campus[cx][cy] != "X":
            if campus[cx][cy] == "P":
                cnt += 1
            campus[cx][cy] = "X"
            stack.append((cx,cy))
if cnt > 0:
    print(cnt)
else:
    print("TT")


