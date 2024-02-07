import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

M = int(input())
lst2 = list(map(int, input().split()))

diff = set(lst2) - set(lst)

# res = [1 if i not in diff else 0 for i in lst2]

for i in lst2:
    if i not in diff:
        print(1)
    else:
        print(0)

# for i in lst2:
#     if i in lst:
#         print(1)
#     else:
#         print(0)

