import sys
input = sys.stdin.readline

N = int(input())
l = len(str(N))
min = float('inf')

for num in range(1,N):
    remain = N-num
    sum = 0
    for ch in str(num):
        sum += int(ch) 
    if num+sum == N and min > num:
        min = num

if min == float('inf'):
    print(0)
else:
    print(min)