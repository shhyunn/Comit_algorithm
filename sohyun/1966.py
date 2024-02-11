import heapq, sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N,M = map(int, input().split())
    lst = list(map(int, input().split()))
    id = [i for i in range(N)]
    cnt = 0

    while True:
        if len(lst) > 1 and lst[0] < max(lst[1:]):
            lst.append(lst.pop(0))
            id.append(id.pop(0))
        else:
            lst.pop(0)
            cnt += 1
            if id.pop(0) == M:
                break
    
    print(cnt)












# prior = []

# for _ in range(T):
#     _,M = map(int,input().split())
#     arr = list(map(int, input().split()))

#     for i in range(len(arr)):
#         heapq.heappush(prior, (-arr[i],i))
    
#     rank = 0
#     seq = -1
#     rank = 0
#     prev = -1
#     same = 1
#     total = 0
#     find = False
#     #119111
#     while True:
#         total += 1
#         pr,seq = heapq.heappop(prior)#pr은 중요도, seq는 순서

#         if seq == M:
#             find = True

#         if prev == pr:
#             same += 1
#             print("same")

#         else: #이전과 다르다면
#             if same > 1: #동점자가 있을 경우
#                 #현재까지 수 - rank 수
#                 print("hi")
#                 rank = total - rank
#             else:
#                 rank += 1
#                 same = 1
        
#         if find and prev != pr:
#             break

#         prev = pr
    
#     print(rank)
