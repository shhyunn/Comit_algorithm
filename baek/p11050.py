N,K = (map(int,input().split()))

def factorial(i):
    num = 1
    for m in range(i):
        num = num * (m+1)
    return num

cal1 = factorial(N)
cal2 = factorial(K) * factorial(N-K)
res = cal1/cal2

print(int(res))