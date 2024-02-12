import sys
input = sys.stdin.readline
N = int(input())
L = input()
hash = 0
for i in range(N):
    hash += (ord(L[i])-96)*(31**i)
hash %= 1234567891
print(hash)