import sys
from collections import deque
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N,M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# max_val = max(max(arr)) -> 첫번쨰 요소가 가장 큰 리스트 반환..
max_val = max(map(max,arr)) #max 함수 매핑->max값 구하기

visited = [[False for _ in range(M)] for _ in range(N)]

direction = [(1,0),(0,-1),(-1,0),(0,1)]

def dfs(k,curr,x,y): #현재 값, k는 현재 몇번 더했는지를 나타냄
    global realMax

    if curr + max_val*(3-k) <= realMax: #현재 curr에서 최댓값을 더해도 realmax값보다 작다면 그만두기
        return
    
    if k == 3: #다 더했을 경우
        realMax = max(realMax,curr) #realmax값 조정
        return
    
    for dx,dy in direction: # 가로, 세로 방향
        cx = x + dx
        cy = y + dy

        if 0 <= cx < N and 0 <= cy < M and not visited[cx][cy]: #아직 방문하지 않았다면
            if k == 1: #십자가 모양 탐색
                visited[cx][cy] = True 
                dfs(k+1, curr+arr[cx][cy],x,y) #다음 방향만을 더하고 탐색 위치는 그대로
                visited[cx][cy] = False
            #다른 모든 모양들 탐색
            visited[cx][cy] = True
            dfs(k+1, curr+arr[cx][cy], cx, cy) #현재의 방향에서 ..?
            visited[cx][cy] = False
    
realMax = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(0,arr[i][j],i,j)
        visited[i][j] = False
print(realMax)