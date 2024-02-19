import sys
input = sys.stdin.readline

#dp
dp = [1,1,1,2,2,3,4,5,7,9]
cnt = 10
T = int(input())
for _ in range(T):
    N = int(input())
    if cnt >= N:
        print(dp[N-1])
    else:
        while cnt != N:
            dp.append(dp[cnt-1]+dp[cnt-5])
            cnt += 1
        print(dp[cnt-1])