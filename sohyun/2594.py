import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N = int(input())
prev = 600
res = 0
dic = [[600,600],[1320,1320]]
for _ in range(N):
    a,b = input().split()
    xa = int(a[:2])*60 + int(a[2:])-10
    xb = int(b[:2])*60+int(b[2:])+10
    dic.append([xa,xb])

# sorted_dic = sorted(dic.items(),key=lambda x:x[0])
dic.sort()
res = 0
prev = 600
for i,j in dic:
    res = max(res, i-prev)
    prev = max(prev,j)

print(res)