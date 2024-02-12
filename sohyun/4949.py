import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
dic = { "(":")","[":"]"}
while True:
    strr = input().rstrip()
    stack = []
    corr = 1
    if strr == ".":
        break
    for i in range(len(strr)):
        if strr[i] in ["(","["]:
            stack.append(strr[i])

        elif strr[i] in [")","]"]:
            if len(stack) == 0 or dic[stack[-1]] != strr[i]:
                corr = 0
                break
            else:
                stack.pop()

    if len(stack) == 0 and corr:
        print("yes")

    else:
        print("no")