from collections import deque

N = int(input())
for _ in range(N):
    strr = str(input())
    lst = list(strr)

    stack = deque([])
    solve = 1
    for ch in lst:
        if len(stack) > 0:
            if ch == "(":
                stack.append(ch)
            elif ch == ")":
                stack.pop()

        else:
            if ch == "(":
                stack.append(ch)
            else:
                solve = 0
                break

    if len(stack) > 0 or solve == 0:
        print("NO")
    else:
        print("YES")