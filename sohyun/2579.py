import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]
max_stairs = [[-1,-1] for _ in range(N)]

max_stairs[0][0] = stairs[0]
max_stairs[0][1] = stairs[0]

for id in range(1,N):
    if id-2 < 0:
        max_stairs[id][0] = stairs[id]
    else:
        max_stairs[id][0] = max(stairs[id]+max_stairs[id-2][0],
                                stairs[id]+max_stairs[id-2][1])
    
    max_stairs[id][1] = stairs[id]+max_stairs[id-1][0]


    
print(max(max_stairs[N-1][0], max_stairs[N-1][1]))