import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N,M,x,y = map(int,input().split())
    k = x
    res = -1
    #k는 왜 n*m보다 작거나 같을까?
    while k <= N*M: #k는 n과 m개의 수 조합으로 표현됨
        if (k-y)%M == 0: #나머지가 0인지 확인하자!
            res = k
            break
        k += N
    print(res)


    # rest = []
    # i = x
    # if N == 1:
    #     if x != 1:
    #         print(-1)
    #     else:
    #         print(y)
    # elif M == 1:
    #     if y != 1:
    #         print(-1)
    #     else:
    #         print(x)
    # else:
    #     while True:
    #         if (i-y) % M == 0:
    #             print(i)
    #             break
    #         if r in rest:
    #             print(-1)
    #             break
    #         i += N
    #         rest.append(r)

