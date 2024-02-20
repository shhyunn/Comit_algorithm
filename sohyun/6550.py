import sys
input = sys.stdin.readline
while True:
    try:
        s,t = input().strip().split()
        #부분문자열 s가 t의 문자열인 경우
        ls, lt = len(s),len(t) 
        i,j = 0,0
        while i < ls and j < lt:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        if i == ls:
            print("Yes")
        else:
            print("No")
    except:
        break