import sys
input = sys.stdin.readline
N = int(input())
dp = [0]*(100001)
dp[1], dp[2] = 3,7
if N <= 2:
    print(dp[N])
else:
    for i in range(3,N+1):
        dp[i] = (dp[i-2] + dp[i-1]*2)%9901
    
    print(dp[N])