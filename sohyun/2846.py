N = int(input())
lst = list(map(int, input().split()))
prev = -1
sum = 0
sum_lst = []
for n in lst:
    if prev < n :
        if prev != -1:
            sum += (n-prev)
        prev = n 
    else:
        sum_lst.append(sum)
        sum = 0
        prev = n

sum_lst.append(sum)

print(max(sum_lst))