import heapq, sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    min_heap = []
    max_heap = []
    exist = [1]*N

    for i in range(N):
        ch, n = input().split()

        if ch == "I":
            heapq.heappush(min_heap,(int(n),i))
            heapq.heappush(max_heap,(-int(n),i))
        else:
            if len(min_heap) == 0:
                continue

            if n == "1":
                #최댓값 삭제
                if max_heap:
                    exist[heapq.heappop(max_heap)[1]] = 0

            else:
                if min_heap:
                    exist[heapq.heappop(min_heap)[1]] = 0
        
        while min_heap and exist[min_heap[0][1]]==0: #최솟값이 이건데, exist가 없네?
            heapq.heappop(min_heap) #최솟값 제거
        
        while max_heap and exist[max_heap[0][1]]==0: #최댓값이 이건데, exist가 없네?
            heapq.heappop(max_heap) #최댓값 제거

    if len(min_heap) == 0:
        print("EMPTY")
    else:
        print(-heapq.heappop(max_heap)[0], end=" ")
        print(heapq.heappop(min_heap)[0])        