import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
n = int(input())
dp = [[0 for _ in range(n)] for _ in range(n+1)]
for i in range(1,n+1):
    lst = list(map(int, input().split()))
    for j,v in enumerate(lst): #0,7
        if j == 0:
            dp[i][j] = dp[i-1][j]+v 
        elif j+1 == i:
            dp[i][j] = dp[i-1][j-1]+v 
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])+v 
print(max(dp[n]))

