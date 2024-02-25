import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
#x를 좌표압축한 결과 xi>xj를 만족하는 xj의 개수와 같다?
#좌표압축한 x'1을 출력
# 2 4 -10 4 -9
# 2 3  0  3  1

set_lst = sorted(set(lst))
dic = {}
for i,j in enumerate(set_lst):
    dic[j] = i #값에 대한 i 인덱스

res = []
for k in lst:
    res.append(dic[k])

print(" ".join(map(str,res)))