import sys
input = sys.stdin.readline
N = int(input())
#카드 n개를 갖기 위해 지불해야 하는 최댓값
#카드 n개 ->pn원
pay = list(map(int, input().split()))

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if j < i:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-i]+pay[i-1])

print(dp[N][N])