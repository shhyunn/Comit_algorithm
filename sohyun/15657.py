import sys
from itertools import combinations_with_replacement
# sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N,M = map(int ,input().split())
arr = list(map(int, input().split()))

arr.sort()

dic = combinations_with_replacement(arr,M)
for com in dic:
    print(" ".join(map(str,com)))