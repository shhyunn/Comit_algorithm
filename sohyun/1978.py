import sys
input = sys.stdin.readline

def count_primes(n,lst):
    count = 0
    mnum = max(lst)
    primes = [1]*(mnum+1)
    primes[0] = 0
    primes[1] = 0

    for i in range(2, mnum+1):
        if primes[i]:
            for k in range(i*i,mnum+1,i):
                primes[k] = 0
                
    for num in lst:
        if primes[num]:
            count += 1
    return count


N = int(input())
lst = list(map(int, input().split()))

print(count_primes(N,lst))
