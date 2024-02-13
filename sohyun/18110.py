#아무 의견이 없을시 난이도 0
#의견이 하나 이상 -> 문제 난이도는 30%절사평균 -> 큰 값과 가장 작은값 제외
import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
n = int(input()) #난이도 의견의 개수, 1이상 30이하 -> 카운팅정렬
rank = [0]*31

def rounded(n):
    if n - int(n) >= 0.5:
        return int(n)+1
    else:
        return int(n)
    
if n == 0:
    res = 0
else:
    minus = rounded((n*0.3)/2)

    for _ in range(n):
        t = int(input())
        rank[t]+=1
    i = 0
    sum = 0
    id = 1
    while i < n: #사람 수
        if rank[id] >= 1:
            for _ in range(rank[id]):#1
                if minus <= i < n-minus:
                    sum += id
                i += 1
        id += 1
    res = rounded(sum/(n-minus*2))

print(res)