X = int(input())
k =1
cnt = 1

while k <= 10000000:
    if k+cnt > X:
        break
    k += cnt
    cnt += 1

X -= k
if cnt % 2 == 1:
    a = cnt
    b = 1
    for i in range(X):
        a -= 1
        b += 1
    print(str(a)+"/"+str(b))

else:
    a = 1
    b = cnt
    for i in range(X):
        a += 1
        b -= 1
    print(str(a)+"/"+str(b))