import sys
input = sys.stdin.readline
lst= [1,2]
i = 2
N = int(input())
res = 0
if N == 1:
    res = 1
elif N >= 2 and N <= 7:
    res = 2
else:
    while True:
        lst.append(lst[i-1] + 6*(i-1))
        if lst[i] > N:
            res = i
            break
        i += 1

print(res)