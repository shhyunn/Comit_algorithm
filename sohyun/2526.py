N, P = map(int, input().split())

temp = N
rest_lst = []

res = 0
while True:
    temp = temp * N % P

    if temp in rest_lst:
        for i in range(len(rest_lst)):
            if temp == rest_lst[i]:
                res = len(rest_lst) - i
        break

    rest_lst.append(temp)
    

print(res)