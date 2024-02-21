import sys
input = sys.stdin.readline
N = int(input())
dp =[0]*1000001
#00타일과 1 타일, N이 주어졌을 때 만들 수 있는 모든 가짓수->dp
i = 3
dp[1],dp[2] = 1,2
if N < i:
    print(dp[N])

else:
    while i <= N:
        dp[i] = (dp[i-1] + dp[i-2])%15746
        i += 1

    print(dp[N])