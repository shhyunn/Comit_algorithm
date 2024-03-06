import sys
input = sys.stdin.readline

#s가 주어질 떄 최소 몇마리의 개구리?
#KKPKPPKKKP, 최대로 이어진 문자열 개수
s = input().strip()

pnum = 0
knum = 0

for ch in s:
    if ch == "P": #p가 필요할 경우
        if knum > 0:
            knum -= 1
            pnum += 1
        else:
           pnum += 1
    
    elif ch == "K":
        if pnum > 0:
           pnum -= 1
           knum += 1

        else:
           knum += 1
    
print(pnum + knum)