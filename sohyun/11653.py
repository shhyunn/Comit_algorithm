#소인수분해
#소인수분해 결과를 한줄에 하나씩 오름차순 출력, 1인경우 출력 x

N = int(input())
div = 2
temp = N
while (div <= (temp ** (1/2) + 1)):
    while (N % div == 0):
        print("%d"%div)
        N //= div
    div += 1

if ( N != 1):
    print("%d"%N)

# N=int(input())
# end=int(N**(1/2))
# for i in range(2,end+1):
#     while N%i==0:
#         print(i)
#         N//=i
# if N!=1:
#     print(N)