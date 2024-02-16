import sys
#input = sys.stdin.readline
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
N,M = map(int, input().split())
dic = {}

for _ in range(N):
    site,pw = input().split()
    dic[site] = pw

for _ in range(M):
    ques = input()
    print(dic[ques])