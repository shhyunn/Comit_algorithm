import sys, heapq
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
start,end = map(int, input().split())
INF = 1e9

def dijkstra(start, end):
    distance = [INF]*(N+1)
    distance[start] = 0
    stack = [(distance[start],start)]
    while stack:
        d,v = heapq.heappop(stack)
        if distance[v] < d:
            continue
        for i,j in graph[v]:
            if d+j < distance[i]:
                distance[i] = d+j
                heapq.heappush(stack,(distance[i],i))
    return distance[end]
print(dijkstra(start,end))

# def dijkstra(start,end):
#     distance = [INF]*(N+1)
#     distance[start] = 0
#     visit = [(distance[start], start)]

#     while visit:
#         vw, vn = heapq.heappop(visit)#도착 지점까지의 거리
#         if distance[vn] < vw: #이미 최소 거리로 되어있음
#             continue
#         for v,e in graph[vn]:
#             if vw + e < distance[v]:
#                 distance[v] = vw + e
#                 heapq.heappush(visit, (vw+e,v))

#     return distance[end]