import sys
input = sys.stdin.readline

N,M,K = map(int, input().split())
dp = [[0 for _ in range(M+1)] for _ in range(N)]

dp[0][1] = 1

for i in range(N):
    for j in range(1,M+1):
        if i != 0:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])+1
        else:
            dp[i][j] = dp[i][j-1]+1

if dp[N-1][M] <= K:
    print("YES")
    for ls in dp:
        print(" ".join(map(str,ls[1:])))

else:
    print("NO")