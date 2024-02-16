import sys
input = sys.stdin.readline

T = int(input())
fibo = [[0,0] for _ in range(41)]
fibo[0][0] += 1
fibo[1][1] += 1

#fibo[0] 과 fibo[1]이 몇번 출력되는지
#0 <= N <= 40

for i in range(2,41):
    fibo[i][0] = fibo[i-1][0] + fibo[i-2][0]
    fibo[i][1] = fibo[i-1][1] + fibo[i-2][1]

for _ in range(T):
    N = int(input())
    print(fibo[N][0],fibo[N][1])