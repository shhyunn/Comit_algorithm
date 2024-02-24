import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N = int(input())

lst = list(map(int, input().split()))
dp = [0]*(N+1)
for i in range(1,N+1):
    id,ll = -1,-1
    for j in range(1,i+1):
        if ll < dp[j] and lst[j-1] < lst[i-1]:
            id = j
            ll = dp[j]
    dp[i] = dp[id] + 1

print(max(dp))