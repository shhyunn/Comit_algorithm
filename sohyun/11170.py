T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    cnt = 0
    for i in range(N, M+1):
        temp = str(i)
        for k in range(len(temp)):
            if temp[k] == '0':
                cnt += 1

    print(cnt)

