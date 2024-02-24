import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

N = int(input())
lst1 = list(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split())) #상근이가 가지고 있음?
dict = {key:0 for key in lst2}
for i in lst1:
    if i in dict.keys():
        dict[i] = 1
for k in dict.items():
    print(k[1], end=" ")
