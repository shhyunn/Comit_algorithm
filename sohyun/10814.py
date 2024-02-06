N = int(input())
dic = {}
for _ in range(N):
    num, name = input().split()
    if int(num) not in dic.keys():
        dic[int(num)] = [str(name)]
    else:
        dic[int(num)].append(str(name))

dic = dict(sorted(dic.items()))

for key, value in dic.items():
    for val in value:
        print("%d %s"%(key,val))