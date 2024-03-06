import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))

#다른게 나오면! 그거의 인덱스 저장
stack = []
res = [0 for _ in range(N)]
curr = -1

for id,num in enumerate(lst):
    if len(stack) > 0 and curr == num:
        stack.append(id)

    else: #다르다면
        while stack:
            q = stack.pop()
            res[q] = id+1
        stack.append(id)
        curr = num

if stack:
    while stack:
        q = stack.pop()
        res[q] = -1

print(" ".join(map(str, res)))