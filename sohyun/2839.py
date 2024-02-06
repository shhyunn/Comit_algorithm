N = int(input())
num3 = N // 3
num5 = N // 5
min = float('inf')

for i in range(num3+1):
    for j in range(num5+1):
        sum = 3*i + 5*j
        if sum == N and min > i+j:
            min = i+j

        if sum >= N:
            break

if min == float('inf'):
    res = -1
else:
    res = min

print(res)