import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

N, M = map(int,input().split())
lst = list(map(int,input().split()))


res = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            sum = lst[i]+lst[j]+lst[k]
            if sum <= M and res < sum:
                res = sum
            
            if res == M:
                break

print(res)

