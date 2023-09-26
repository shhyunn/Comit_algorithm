num1 = int(input())

list1 = list(map(int,input().split()))
list1.sort()
minimum = int(list1[0])
maximum = int(list1[num1-1])
res = minimum * maximum
print(res)