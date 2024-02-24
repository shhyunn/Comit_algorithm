import sys
input = sys.stdin.readline

N = int(input())
lst = [-1]*(N//2)
ans = 0
def promise(x):
    for i in range(x):
        if lst[x] == lst[i] or abs(lst[x] - lst[i]) == abs(x-i):
            return False
    return True

def n_queen(x):
    global ans
    if x == N//2:
        ans += 1
        return
    
    for i in range(N):
        lst[x] = i
        if promise(x):
            n_queen(x+1)
n_queen(0)
print(ans*2)