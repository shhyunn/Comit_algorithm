import sys
input = sys.stdin.readline
n = int(input())

dp = [0,1,3,5]
cnt = 3
if n <= cnt:
    print(dp[n]%10007)
else:
    while n != cnt:
        cnt += 1
        dp.append(dp[cnt-1] + dp[cnt-2]*2)
    print(dp[n]%10007)