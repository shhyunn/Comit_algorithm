import sys
input = sys.stdin.readline

mul = [1]*11
for i in range(1,11):
    mul[i] = i*mul[i-1]

T = int(input())

def collabo(i,j,k):
    total = i+j+k
    res = mul[total] // mul[i]
    res //= mul[j]
    res //= mul[k]
    return res

for _ in range(T):
    N = int(input())
    sum = 0

    for i in range(N//3+1): #3개수
        for j in range(N//2+1): #2개수
            for k in range(N+1): #1개수
                temp = 3*i + 2*j + k
                if  temp > N:
                    break

                if temp == N:
                    sum += collabo(i,j,k)
                    break

            if temp > N:
                break

    print(sum)

'''
n = int(input())
n_list = [int(input()) for _ in range(n)]
d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4
d[4] = 7

for i in range(5, 11):
    d[i] = d[i-3] + d[i-2] + d[i-1]

for j in n_list:
    print(d[j])
'''