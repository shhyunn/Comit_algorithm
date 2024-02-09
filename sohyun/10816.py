import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

N = int(input())
lst1 = list(map(int,input().split()))

M = int(input())
lst2 = list(map(int, input().split()))

dic = {key:0 for key in lst2}

for n in lst1:
    if n in dic.keys():
        dic[n] += 1

#print(" ".join(map(str,dic.values())))

for res in lst2:
    print(dic[res], end=" ")