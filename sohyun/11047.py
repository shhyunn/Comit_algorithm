import sys
input = sys.stdin.readline

N,K = map(int,input().split())

coin = [int(input()) for _ in range(N)]
total = K
res = 0

for i in range(-1,-(N+1),-1):
    res += total // coin[i]
    total= total % coin[i]
    if total == 0:
        break

print(res)