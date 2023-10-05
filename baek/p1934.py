import math
res = []
num = int(input())
for i in range(num):
    A,B = (map(int,input().split()))
    cal = math.lcm(A,B)
    res.append(cal)

for i in range(num):
    print(res[i])
