import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

def sub(s1,s2,e1,e2):
    if e1-s1 == 1 and e2-s2 == 1:
        if paper[s1][s2] == 1:
            return (0,1)
        else:
            return (1,0)
    
    mid1 = (s1+e1)//2
    mid2 = (s2+e2)//2
    
    r1 = sub(s1,s2,mid1,mid2)
    r2 = sub(mid1,s2,e1,mid2)
    r3 = sub(s1,mid2,mid1,e2)
    r4 = sub(mid1,mid2,e1,e2)

    if r1 == r2 == r3 == r4 == (0,1):
        return (0,1)
    elif r1 == r2 == r3 == r4 == (1,0):
        return (1,0)
    
    else:
        return (r1[0]+r2[0]+r3[0]+r4[0],r1[1]+r2[1]+r3[1]+r4[1])

a,b = sub(0,0,N,N)
print(a)
print(b)