T = int(input())
for _ in range(T):
    N = int(input())
    max_L = 0
    max_S = ''
    for _ in range(N):
        S, L = input().split()
        S = str(S)
        L = int(L)
        if max_L < L:
            max_L = L
            max_S = S
    
    print(max_S)