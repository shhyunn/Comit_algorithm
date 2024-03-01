import sys
from itertools import permutations
# sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

N,M = map(int, input().split()) #n개의 자연수에서 m개를 고른 수열
nums = sorted(list(map(int, input().split())))

dic = list(permutations(nums,M))
for com in dic:
    print(" ".join(map(str,com)))