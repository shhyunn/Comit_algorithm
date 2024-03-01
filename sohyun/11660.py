import sys

sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

#노드, 왼쪽노드, 오른쪽 노드
N,M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = dp[i-1][j] + arr[i-1][j-1]
        # dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]

for _ in range(M):
    x1,y1,x2,y2 = map(int, input().split())
    total = 0
    for n in range(y1,y2+1):
        total += (dp[x2][n]-dp[x1-1][n])
        # result = dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
    print(total)