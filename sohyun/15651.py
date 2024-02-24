import sys
input = sys.stdin.readline
N,M = map(int,input().split())

res = []
def bfs(x):
    if len(res) == M:
        print(" ".join(map(str,res)))
        return
    
    for i in range(1,N+1):
        res.append(i)
        bfs(i+1)
        res.pop()

bfs(1)