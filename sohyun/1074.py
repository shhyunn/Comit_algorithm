import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

N,r,c = map(int, input().split())

def find(s1,s2,e1,e2,r,c,cnt,n):
    if n == 1:
        return cnt
    mid1 = (s1+e1) // 2
    mid2 = (s2+e2) // 2
    n //= 2 #4
    if r < mid1 and c < mid2: #1사분면
        return find(s1,s2,mid1,mid2,r,c,cnt,n)

    elif r < mid1 and mid2 <= c: #2사분면
        return find(s1,mid2,mid1,e2,r,c,cnt+n*n,n)

    elif r >= mid1 and c < mid2: #3사분면
        return find(mid1,s2,e1,mid2,r,c,cnt+n*n*2,n)

    elif r >= mid1 and c >= mid2: #4사분면
        return find(mid1,mid2,e1,e2,r,c,cnt+n*n*3,n)

print(find(0,0,2**N,2**N,r,c,0,2**N))