import sys
from collections import deque
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N,M = map(int, input().split()) #1,1부터 n,m까지
mirro = []
for _ in range(N):
    mirro.append(list(input().rstrip()))

stack = deque([(0,0,1)])
mirro[0][0] = "0"
dx = [-1,1,0,0]
dy = [0,0,-1,1]
res = -1
while len(stack) != 0:
    a,b,d = stack.popleft()
    if a == N-1 and b == M-1:
        res = d
        break

    for i in range(4):
        cx = a + dx[i]
        cy = b + dy[i]

        if 0 <= cx < N and 0 <= cy < M and mirro[cx][cy] == "1":
            stack.append((cx,cy,d+1))
            mirro[cx][cy] = "0"

print(res)



