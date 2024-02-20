import sys
input = sys.stdin.readline
#라그랑주 : 제곱수들의 합
# n을 최소 개수의 제곱수 합으로 표현하는 컴퓨터 프로그램 작성-> 최소개수 출력
def is_squared(n):
    return n == int(n**0.5)**2

def main(n):
    if is_squared(n):
        return 1
    
    for i in range(1,int(n**0.5)+1):
        if is_squared(n-i**2):
            return 2
        
    for i in range(1,int(n**0.5)+1):
        for j in range(1,int((n-i**2)**0.5)+1):
            if is_squared(n-i**2-j**2):
                return 3

    return 4 #라그랑주는 반드시 4개 이하의 제곱수로 나눠진다!!
                
N = int(input())
print(main(N))

# dp = [0,1,2,3]
# k = 2
# i = 4
# if N <= 3:
#     print(dp[N])

# else:
#     sum = 4
#     next = 9
#     while True:
#         min = 99999
#         for m in range(1,k+1):
#             if dp[i-m**2]+1 < min:
#                 min = dp[i-m**2] + 1

#         dp.append(min)

#         if i == N:
#             break
#         i += 1

#         if i == next:
#             k += 1
#             sum = next
#             next = (k+1)**2
        
#     print(dp[N])