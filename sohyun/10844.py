#길이가 N인 계단수가 몇개, 모든 자리 차이가 1
import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(9)

else:
    dp = [[0 for _ in range(12)] for _ in range(N+1)] #-1과 10 추가

    for k in range(2,11): #1부터 9까지 더하기
        dp[1][k] = 1

    for i in range(2,N+1): #자릿수, 2부터 시작
        for j in range(1,11): #0~10 합
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])

    print(sum(dp[N])%1000000000)