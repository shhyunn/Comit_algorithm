import sys
input = sys.stdin.readline
strr = input().rstrip()

prev = -1
back = 0
res = 0
for i in strr:
    if i == "(":
        if prev == 0:
            back += 1
        else:
            prev = 0
    else:
        if prev == 1:
            res += back
        else:
            prev = 1
print(res)
