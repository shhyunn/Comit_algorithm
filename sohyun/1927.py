import sys
import heapq
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(stack,x)
    elif x == 0:
        if len(stack) == 0:
            print(0)
            continue
        print(heapq.heappop(stack))

