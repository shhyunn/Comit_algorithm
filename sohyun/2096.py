import sys, heapq
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
#숫자 표에서 얻을 수 있는 최대점수와 최소점수
N = int(input())
arr = list(map(int, input().split()))
max_dp = arr
min_dp = arr

for _ in range(N-1):
    arr = list(map(int, input().split()))
    max_dp = [arr[0]+max(max_dp[0],max_dp[1]), arr[1]+max(max_dp[0],max_dp[1],max_dp[2]), arr[2]+max(max_dp[1],max_dp[2])]
    min_dp = [arr[0]+min(min_dp[0],min_dp[1]), arr[1]+min(min_dp[0],min_dp[1],min_dp[2]), arr[2]+min(min_dp[1],min_dp[2])]

print(max(max_dp),min(min_dp))
'''
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(1,N+1): #N개의 줄
    max_0 = max(dp[0],dp[1])
    max_1 = max(dp[0],dp[1],dp[2])
    max_2 = max(dp[1],dp[2])
    dp[0] = max_0 + arr[i-1][0]
    dp[1] = max_1 + arr[i-1][1]
    dp[2] = max_2 + arr[i-1][2]

max_val = max(dp)
dp = [0,0,0]
for i in range(1,N+1):
    min_0 = min(dp[0],dp[1])
    min_1 = min(dp[0],dp[1],dp[2])
    min_2 = min(dp[1],dp[2])
    dp[0] = min_0 + arr[i-1][0]
    dp[1] = min_1 + arr[i-1][1]
    dp[2] = min_2 + arr[i-1][2]

min_val = min(dp)
print(max_val, min_val)
'''
#슬라이딩 윈도우!! -> 사용하지 않는 값을 배열에 저장하지 않음