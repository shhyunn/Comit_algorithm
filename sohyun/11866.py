import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())

arr = [str(i) for i in range(1,N+1)]
arr = deque(arr)

res = []
while arr:
    for i in range(K-1):
        arr.rotate(-1)
    res.append(arr.popleft())

fg = ", ".join(res)
print("<"+fg+">")