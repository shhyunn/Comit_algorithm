import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N,M = map(int, input().split())
hear_lst = []
see_lst = []

for _ in range(N):
    hear = input().strip()
    hear_lst.append(hear)

for _ in range(M):
    see = input().strip()
    see_lst.append(see)

hear_set, see_set = set(hear_lst), set(see_lst)
sum = hear_set & see_set

print(len(sum))
for name in sorted(sum):
    print(name)
