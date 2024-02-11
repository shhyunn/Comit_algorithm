import sys
input = sys.stdin.readline

N = int(input())
stack = [] #오름차순으로 쌓을 스택
res = ""

arr = [int(input()) for _ in range(N)]

push = 1
flag = True
for num in arr: #수열에 있는 숫자대로
    while push <= num:
        stack.append(push)
        res += "+"
        push += 1

    if stack[-1] == num:
        stack.pop()
        res += "-"

    else:
        print("NO")
        flag = False
        break

if flag == True:
    for ch in res:
        print(ch)