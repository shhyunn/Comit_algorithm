a, b, c, d, e = map(int, input().split())
num_lst = [a, b, c, d, e]
res = [1, 2, 3, 4, 5]
while num_lst != res :
    for i in range(4):
        if num_lst[i] > num_lst[i+1]:
            num_lst[i], num_lst[i+1] = num_lst[i+1], num_lst[i]
            print("%d %d %d %d %d"%(num_lst[0], num_lst[1], num_lst[2], num_lst[3], num_lst[4]))