import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

lst.sort()
lst.sort(key=lambda lst:lst[1])

for arr in lst:
    print("%d %d"%(arr[0],arr[1]))