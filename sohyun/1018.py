import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

N,M = map(int, input().split())
arr = []
for i in range(N):
    strr = list(str(input()))
    temp = [1 if ch == "B" else 0 for ch in strr]
    arr.append(temp)

min = float("inf")
for i in range(N-8+1):
    for j in range(M-8+1):
        sum = 0
        num = arr[i][j] #0
        opp = 0
        for k in range(i,i+8): #0부터 8
            for l in range(j,j+8): #0부터 8
                if arr[k][l] != num:
                    sum += 1
                num = not(num)
            num = not(num)
        opp += (64-sum)
        if opp < min:
            min = opp
        if sum < min:
            min = sum

print(min)