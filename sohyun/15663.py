import sys
from itertools import permutations
# sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N,M = map(int ,input().split())
arr = list(map(int, input().split()))
dic = sorted(set(permutations(arr,M)))

for com in dic:
    print(" ".join(map(str, com)))
#sys.stdout.write()