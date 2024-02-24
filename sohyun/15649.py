import sys

input = sys.stdin.readline
N,M = map(int, input().split())
res = []
def bfs(lst):
    if len(res) == M:
        print(" ".join(map(str,res)))
        return
    
    for i in lst:
        res.append(i)
        new = lst[:]
        new.remove(i)
        bfs(new)
        res.pop()

        
lst = [i for i in range(1,N+1)]
bfs(lst)

# # n, m = list(map(int, input().split()))
# # num = []

# # def dfs():
# #     if len(num) == m:
# #         print(" ".join(map(str, num)))
# #         return
    
# #     for i in range(1, n + 1):
# #         if i not in num:
# #             num.append(i)
# #             dfs()
# #             num.pop()
# # dfs()