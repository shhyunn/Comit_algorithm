N = int(input())
data = []
for _ in range(N):
    w,h = map(int, input().split())
    data.append([w,h])

res = []

for i in range(N):
    cnt = 1
    for j in range(N):
        if data[j][0] > data[i][0] and data[j][1]> data[i][1]:
            cnt += 1   
    res.append(cnt)

for r in range(N):
    # if r != 0:
    #     print("")
    print("%d "%res[r], end="")
