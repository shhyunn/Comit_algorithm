import sys,heapq
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(stack,-x)
    else:
        if len(stack) == 0:
            print(0)
        else:
            num = heapq.heappop(stack)
            print(-num)