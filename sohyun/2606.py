import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N = int(input())
M = int(input())
visited = [0]*(N+1)
connect = {key:[] for key in range(1,N+1)}

for _ in range(M):
    a,b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

stack = [1]
cnt = 0
while stack != []:
    i = stack.pop() #1 pop
    if not visited[i]:
        stack += connect[i]
        visited[i] = 1
        cnt += 1

print(cnt-1)