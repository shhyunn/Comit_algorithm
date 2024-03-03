import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

#재귀!!!
graph = []
while True:
    try:
        graph.append(int(input()))
    except:
        break

# graph = [50,30,24,5,28,45,98,52,60]

def postorder(start, end):
    if start > end:
        return
    
    mid = end+1 #end+1로 설정, 루트보다 큰 값이 없을 경우 고려
    for i in range(start+1, end+1):
        if graph[start] < graph[i]:
            mid = i
            break
    
    postorder(start+1, mid-1)
    postorder(mid, end)
    print(graph[start])

postorder(0,len(graph)-1)

# def postorder(first, end):
#     if first > end:
#         return
    
#     mid = end + 1
#     for i in range(first+1, end+1): #처음은 루트노드, 마지막 노드까지
#         if graph[first] < graph[i]: #현재의 루트노드보다 큰 값이 나올 경우
#             mid = i
#             break
#     #print(mid, first, end)

#     postorder(first+1, mid-1) #left
#     postorder(mid, end) #right
#     print(graph[first]) #v

# postorder(0, len(graph)-1) #처음 인덱스랑 마지막인덱스






    