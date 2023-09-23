N, K = map(int, input().split( ))

res = 1
upper = 1
lower = 1
for i in range(K):
    upper *= (N-i)

for i in range(K):
    lower *= (K-i)

res = upper // lower
print(int(res))

