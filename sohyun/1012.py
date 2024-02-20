import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(T):
    M,N,K = map(int,input().split())
    arr = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        i,j = map(int, input().split())
        arr[i][j] = 1
    
    #bfs
    ans = 0

    for i in range(M):
        for j in range(N):
            if arr[i][j] == 0:
                continue

            stack = [(i,j)] #1일 경우
            while stack:
                a,b = stack.pop()
                for k in range(4):
                    a1 = a + dx[k]
                    b1 = b + dy[k]
                    if 0 <= a1 < M and 0 <= b1 < N and arr[a1][b1] == 1:
                        stack.append((a1,b1))
                        arr[a1][b1] = 0
            ans += 1

    print(ans)