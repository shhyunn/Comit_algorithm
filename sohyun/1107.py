import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N = int(input())
M = int(input())
error = list(map(int, input().split()))

min_count = abs(100 - N)
#브루트포스 알고리즘
for nums in range(1000001):
    nums = str(nums)
    # for j in range(len(nums)):
    #     if int(nums[j]) in error:
    #         break
    #     elif j == len(nums) -1:
    #         min_count = min(min_count, abs(int(nums) - N)+len(nums))
    i = 0
    while i != len(nums):
        if int(nums[i]) in error:
            break
        i += 1
    if i == len(nums):
        min_count = min(min_count,len(nums)+abs(N-int(nums)))

print(min_count)
        
     





# error = []
# nums = [1 for _ in range(10)]
# if M > 0:
#     error = list(map(int, input().split()))
#     for i in error:
#         nums[i] = 0

# rest = set([i for i in range(10)]) - set(error)
# if len(rest) == 0:
#     print(abs(int(N)-100))

# else:
#     max_num = max(rest)
#     min_num = min(rest)

#     # minmax = [[] for _ in range(10)]
#     # for n in range(-1,-11,-1):
#     #     if nums[n-1] == 1:
#     #         minmax[n][0] = n-1

#     cnt = 0
#     res = ""
#     ll = len(N)
#     min_val = -1
#     max_val = -1

#     for i,ch in enumerate(N):
#         n = int(ch)
#         if nums[n] == 1:
#             cnt += 1
#             res += ch

#         else: #같지 않다면
#             mini,maxi = n,n
#             while mini >= 0 and nums[mini] != 1:
#                 mini -= 1

#             while maxi < 10 and nums[maxi] != 1:
#                 maxi += 1

#             if mini >= 0 or maxi < 10:
#                 if mini >= 0:
#                     min_val = int(res + str(mini) + str(max_num)*(ll-i-1))
            
#                 if maxi < 10:
#                     max_val = int(res + str(maxi) + str(min_num)*(ll-i-1))

#                 cnt += ll-i
#             break
#     print(cnt)
#     N = int(N)
#     if len(res) == ll:
#         print(min(cnt,abs(N-100)))

#     else:
#         res_cnt = abs(N - 100)
#         if min_val != -1:
#             res_cnt = min(res_cnt,cnt+(N-min_val))
#         if max_val != -1:
#             res_cnt = min(res_cnt, cnt+(max_val-N))

#         print(res_cnt)