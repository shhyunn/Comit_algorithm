import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N,M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1,max(trees)

while start <= end: #start와 end 사이에 다른 칸이 존재하는지 확인
    mid = (start+end)//2
    sums = 0
    for i in trees:
        if i > mid:
            sums += (i - mid) 
    if sums >= M:
        #현재 mid는 최솟값과 최댓값의 중간, sums가 더 크다면d, mid를 1증가시키자. mid의 구간은 start ~ end에서 mid+1 ~ end
        start = mid+1 
    else:
        end = mid-1 #sums가 M보다 작을 경우, mid의 구간은 start ~ end에서 start ~ mid-1이 된다, mid 이상부터는 될 수 없음!

print(end) #절단기에 설정할 수 있는 높이의 최댓값

# def find(mid,prev,sums):
#     if mid < 0 or mid > sums:
#         return prev
    
#     temp = 0
#     for i in range(-1,-N-1,-1):
#         if trees[i] <= mid:
#             break
#         temp += (trees[i] - mid)

#     if temp > M: #temp가 mid보다 크다면, 그러니까 더 많이 잘랐다면
#         return find(mid+1,max(prev,mid),sums)
    
#     elif temp == M:
#         return mid
    
#     else: #temp가 M보다 덜 잘랐다면, mid를 낮추자!
#         return find(mid-1,prev,sums)
    
# print(find((trees[0]+trees[-1])//2,0,sum(trees)))