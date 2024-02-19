import sys
input = sys.stdin.readline

dp = [0,1,2]
cnt = 2
N = int(input())
if N <= cnt:
    print(dp[N])
else:
    while cnt != N:
        cnt += 1
        dp.append(dp[cnt-1]+dp[cnt-2])

    print(dp[N]%10007)
    