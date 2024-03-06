import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
prev = arr[0]
max_id = 0
sums = 0
for i in range(1,N):
    if arr[i] < prev:
        sums += 1
    else:
        max_id = max(max_id,sums)
        sums = 0
        prev = arr[i]
max_id = max(max_id, sums)
print(max_id+1)