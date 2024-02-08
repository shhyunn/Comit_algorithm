import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
lst =[i for i in range(N,0,-1)]
lst = deque(lst)

while len(lst)!=1:
    lst.pop()
    lst.appendleft(lst.pop())

print(lst[0])