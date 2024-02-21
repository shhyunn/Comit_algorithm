import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

N = int(input())
dp = [[0,0,0] for _ in range(N+1)]
house = [[0,0,0]]
for _ in range(N):
    house.append(list(map(int, input().split())))
for i in range(1,N+1):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2])+house[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2])+house[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1])+house[i][2]

print(min(dp[N]))




