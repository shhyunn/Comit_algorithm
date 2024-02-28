import sys
from collections import deque
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A,B = map(int, input().split())
    visited = [False]*10000
    stack = deque([(A,"")])
    #명령어 나열 dslr
    visited[A] = True
    while stack:
        x, com = stack.popleft()
        if x == B:
            print(com)
            break
        str_x = (4-len(str(x)))*"0" + str(x)

        r_x = int(str_x[-1]+str_x[:-1])
        if not visited[r_x]:
            stack.append((r_x,com+"R"))
            visited[r_x] = True

        l_x = int(str_x[1:]+str_x[0])
        if not visited[l_x]:
            stack.append((l_x,com+"L"))
            visited[l_x] = True
            
        if int(str_x) == 0:
            s_x = 9999
        else:
            s_x = int(str_x) -1

        if not visited[s_x]:
            stack.append((s_x,com+"S"))
            visited[s_x] = True

        d_x = (int(str_x) * 2) % 10000
        if not visited[d_x]:
            stack.append((d_x,com+"D"))
            visited[d_x] = True