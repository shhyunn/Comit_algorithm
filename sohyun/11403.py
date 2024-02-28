import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

#i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하기
#bfs
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

def bfs(x):
    visited = [0]*N #[0,0,0]
    stack = [x]

    while stack:
        i = stack.pop() #0,0
        for k in range(N):
            if graph[i][k] == 1 and visited[k] == 0:
                visited[k] = 1
                stack.append(k)

    return " ".join(map(str,visited))

for i in range(N):
    print(bfs(i)) #0번째 줄