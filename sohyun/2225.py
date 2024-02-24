import sys
input = sys.stdin.readline

N,K = map(int, input().split())

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
dp[0][0] = 1 #합 0일 때 0개 선택 1

for i in range(N+1):
    for j in range(1,K+1):
        #i : 합이 i가 될 때, j: k개
        dp[i][j] = dp[i-1][j] + dp[i][j-1] #합-1일 때 j개, 합 i이면서 j-1개일 때 dp[i][j], 합 n일 때 k개를 선택하는 경우의 수

print(dp[N][K]%1000000000)
#n=20, k=5라면
#0+20을 4개로, 1+19를 4개로,...20+0을 4개로