import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

N,K = map(int, input().split())
bags = []
for _ in range(N):
    w,v = map(int, input().split())
    bags.append((w,v))

#물건 가치의 최댓값!
#준서가 버틸수 있는 무게*물품의 수
#bags.sort() #굳이 안해도 될듯
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1,N+1): #물품이 바뀜
    cw = bags[i-1][0]
    cv = bags[i-1][1]
    for j in range(1,K+1): #무게가 달라질 때
        if cw > j:
            dp[i][j] = dp[i-1][j]
            continue
        #무게가 들어갈 수 있는 경우
        dp[i][j] = max(dp[i-1][j-cw]+cv, dp[i-1][j])

print(dp[N][K])