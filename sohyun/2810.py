N = int(input())
info = str(input())

num = 0
love_cnt = 0
for ch in info:
    if ch == 'S':
       num += 1

    else:
        if love_cnt == 0:
            love_cnt += 1
            num += 1
        elif love_cnt == 1:
            love_cnt = 0

num += 1

res = 0
if N < num:
    print(N)
else:
    print(num)
