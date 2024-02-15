import sys
sys.stdin = open("C:\\Users\\LG\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
M = int(input())
S = [0]*21

for _ in range(M):
    strr = input().rstrip()
    if strr.startswith("add"):
        n = int(strr[-1])
        S[n] = 1

    elif strr.startswith("remove"):
         n = int(strr[-1])
         S[n] = 0

    elif strr.startswith("check"):
        n = int(strr[-1])
        print(S[n])
    
    elif strr.startswith("toggle"):
        n = int(strr[-1])
        if S[n] == 1:
            S[n] = 0
        else:
            S[n] = 1

    elif strr.startswith("all"):
        S = [1]*21
    elif strr.startswith("empty"):
        S = [0]*21