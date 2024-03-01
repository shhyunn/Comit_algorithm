import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
N,M = map(int ,input().split())
arr = sorted(list(set(map(int, input().split()))))

for com in combinations_with_replacement(arr,M):
    print(" ".join(map(str,com)))