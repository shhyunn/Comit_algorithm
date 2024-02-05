N = int(input())
num = {}
for _ in range(N):
    a,b = map(int, input().split())
    if a not in num:
        num[a] = [b]
    else:
        num[a].append(b)

num = dict(sorted(num.items()))

for key in list(num.keys()):
    temp = sorted(num[key])
    for val in temp:
        print("%d %d"%(key,val))
