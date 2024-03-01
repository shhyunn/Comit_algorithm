import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    sticker = []
    N = int(input())
    for _ in range(2):
        sticker.append([0]+list(map(int, input().split())))

    dp = [[0 for _ in range(N+1)] for _ in range(2)]


    for j in range(1,N+1):
        if j >= 2:
                dp[0][j] = max(dp[0][j-2],dp[1][j-1],dp[1][j-2])+sticker[0][j]
                dp[1][j] = max(dp[0][j-2],dp[0][j-1],dp[1][j-2])+sticker[1][j]
        else:
                dp[0][j] = sticker[0][j]
                dp[1][j] = sticker[1][j]

    print(max(dp[0][N],dp[1][N]))