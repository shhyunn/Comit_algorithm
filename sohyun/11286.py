import sys,heapq
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
#절댓값이 가장 작은 값 출력 후 제거
N = int(input())
q = []
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(q,(abs(x),x))
    else:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])