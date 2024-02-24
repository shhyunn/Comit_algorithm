import sys
input = sys.stdin.readline
#n가지 종류, 가치의 합이 k원
n,k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

#경우의 수 구하기
dp = [0 for _ in range(k+1)]
dp[0] = 1
for i in coin:#동전 원의 값부터 경우의 수 +
    for j in range(i,k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

print(dp[k])