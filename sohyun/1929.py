import sys,math
input = sys.stdin.readline

M,N= map(int,input().split())
prime = [1]*(N+1)
prime[0],prime[1] = 0,0

for i in range(2,int(math.sqrt(N))+1):
    if prime[i]:
        for n in range(i*i,N+1,i):
            prime[n] = 0

for i in range(M,N+1):
    if prime[i]:
        print(i)