import sys
#브루트포스 알고리즘
#시간초과날때는 공간을 활용하자.. 256이 최대였음
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N,M,B =map(int,input().split())
ground = []

for _ in range(N):
    ground += list(map(int,input().split())) #m개의 정수로 땅의 높이

h_lst = [0]*257
for i in ground:
    h_lst[i] += 1

min_h = min(ground)
max_h = max(ground)

prev_t, prev_h = float('inf'),-1

for h in range(min_h,max_h+1):
    need = 0
    over = 0
    for i in range(257):
        if i < h: #높이 개수
            need += (h-i)*h_lst[i]
        else:
            over += (i-h)*h_lst[i]

    if over + B >= need:
        time = need + over*2
        if time <= prev_t:
            prev_t = time
            prev_h = h

print(prev_t, prev_h)

# def binary(arr,start,end,prev,B,calculate):
#     prev_t,prev_h = prev
#     if start > end:
#         return prev
       
#     mid = (start+end) // 2

#     if calculate[mid] == 1:
#         return prev
    
#     if mid > 256 or mid < 0:
#         return prev
    
#     temp = arr
#     pos = 0 #쌓아야돼
#     neg = 0 #제거해야돼
#     calculate[mid] = 1
#     for i in range(len(temp)):
#         num = mid - temp[i]
#         if num >= 0:
#             pos += num
#         else:
#             neg += num

#     if pos > -neg + B:
#         return prev
    
#     else:
#         sum = (-neg)*2+pos #sum은 시간, mid는 높이

#         if sum < prev_t:
#             prev_t = sum
#             prev_h = mid

#         elif sum == prev_t and prev_h < mid:
#             prev_h = mid

#         a,b = binary(arr,start+1,end,(prev_t,prev_h),B,calculate)
#         c,d = binary(arr,start,end-1,(prev_t,prev_h),B,calculate)

#         if a < c:
#             return (a,b)
        
#         elif a > c:
#             return (c,d)
#         else:
#             if b > d:
#                 return (a,b)
#             else:
#                 return (c,d)
            
# ground.sort()
# min_h = ground[0]
# max_h = ground[-1]

# calculate = {key:0 for key in range(min_h,max_h+1)}
# h_lst = calculate.keys()
# t,h = binary(ground,min(ground)-1,max(ground)+1,(float('inf'),-1),B,calculate)
# print("%d %d"%(t,h)) 