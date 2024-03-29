import sys
input = sys.stdin.readline

n = int(input())

dp = [1]*10
for i in range(n-1):
    for j in range(1,10):
        dp[j] += dp[j-1]
print(sum(dp)%10007)

'''
dp = [1] * 10 #0부터 9까지 끝나는 오르막 수 개수, 초기에 1로 설정

for i in range(n-1):#n이 2일 경우
    for j in range(1, 10):
        dp[j] += dp[j-1] #현재 숫자로 끝나는 오르막 개수에 이전 숫자로 끝나는 오르막 개수 더하기 
        #1로 끝나는 수가 01 11, 이전에 0으로 끝나는 수 + 1
        #001 011 111
        #2로 끝나는 수 : 02,12,22
        #022 122 222 002 012 112
        #원래 2로 끝나는 수에 2를 붙인 수 + 원래 1로 끝나는 수에 1을 2로 바꾼 수
        #3로 끝나는 수 3 + 02 + 12 + 22
        #dp[0] = 1, dp[1] = 2, dp[2] = 3, dp[3] = 4

print(sum(dp) % 10007)
'''