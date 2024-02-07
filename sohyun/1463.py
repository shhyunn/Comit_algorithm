import sys
input = sys.stdin.readline

n = int(input())

dp = [-1] * (n+1)
dp[0] = 0
dp[1] = 0

def dps(n):
    if dp[n] != -1:
        return dp[n]
    
    if n % 6 == 0:
        dp[n] = min(dps(n//3), dps(n//2)) + 1

    elif n % 3 == 0:
        dp[n] = min(dps(n//3), dps(n-1)) + 1

    elif n % 2 == 0:
        dp[n] = min(dps(n//2), dps(n-1)) + 1

    else:
        dp[n] = dps(n-1) + 1
    return dp[n]

print(dps(n))

#bottom-up
# import sys
# input = sys.stdin.readline
# N = int(input())

# dp = [0]*(N+1)

# def dps(n):
#     dp[0] = 0
#     dp[1] = 0
#     for i in range(2,n+1):
#         if i % 6 == 0:
#             dp[i] = min(dp[i//3],dp[i//2])+1
#         elif i % 3 == 0:
#             dp[i] = min(dp[i//3],dp[i-1])+1
#         elif i % 2 == 0:
#             dp[i] = min(dp[i//2],dp[i-1])+1
#         else:
#             dp[i] = dp[i-1]+1

#     return dp[n]

# print(dps(N))


