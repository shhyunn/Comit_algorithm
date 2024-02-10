import sys
input = sys.stdin.readline

def max(a,b):
    while b != 0:
        a, b = b,a%b
    return a

N,M = map(int,input().split())

d = max(N,M)
print(d)
print(d*(N//d)*(M//d))