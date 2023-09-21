#a층의 b호에 살려면 자신의 아래층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 함
#비어있는 집은 없음
#첫번째 줄에는 test case:T
#각각 케이스마다 첫번째 줄에는 정수 k, 두번쨰 줄에는 정수 n
#k는 층, n호
#example1: 1층에 3호면 0층의 1+2+3
#example2: 2층의 3호면 1층의 1호 + 2호 + 3호

T = int(input())

# def func(a, b):
#    res = 0
#    if (a == 0):
#     return b
   
#    else:
#     for i in range(1,b+1):
#         res += func(a-1, i)
#     return res

def func2(a,b):
    arr = [[] for _ in range(a+1)]
    for i in range(b):
        arr[0].append(i+1) #0층
    
    for m in range(a):
         arr[m+1].append(1)

    for j in range(1,a+1):
        for k in range(1,b):
            arr[j].append(arr[j][k-1] + arr[j-1][k])

    return arr[a][b-1]

for _ in range (T):
    k = int(input())
    n = int(input())

    print(func2(k,n))

