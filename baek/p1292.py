list1 = []
i = 1
num = 1
res = 0
while True:
    while i > 0:
        list1.append(num)
        i -= 1
        if len(list1) == 1000:
            break
    num += 1
    i = num
    if len(list1) == 1000:
        break

A,B = (map(int,input().split()))

while A <= B:
    res += list1[A-1]
    A += 1

print(res)