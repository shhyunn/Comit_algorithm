import sys
from collections import Counter
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

#다른 알파벳 개수, 세사람 사이의 심리적 거리,a&b,b&c c&a
T = int(input())
for _ in range(T):
    N = int(input())
    feelings = list(input().split())
    # dic = dict(Counter(feelings))
    # sort_dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    # if sort_dic[0][1] >= 3:
    #     print(0)
    if N > 32:
        print(0)
    else:
        min_val = 999999
        for i in range(N-2):
            for j in range(i+1,N-1):
                for k in range(j+1,N):
                    temp = 0
                    for c in range(4):
                        if not(feelings[i][c] == feelings[j][c] == feelings[k][c]):
                            temp += 2

                    if min_val > temp:
                        min_val = temp

        print(min_val)
