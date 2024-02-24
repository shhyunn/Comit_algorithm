import sys
input = sys.stdin.readline

reg = [[[-1 for _ in range(21)] for _ in range(21)] for _ in range(21)]      
def w(a,b,c):
    global regb  
    if a <= 0 or b <= 0 or c <= 0:
          return 1
    elif a > 20 or b > 20 or c > 20:
         return w(20,20,20)
    elif reg[a][b][c] != -1:
         return reg[a][b][c]
    elif a < b and b < c:
         reg[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1)-w(a,b-1,c)
    else:
         reg[a][b][c] = w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return reg[a][b][c]


    
while True:
        a,b,c = map(int, input().split())
        if a == -1 and b == -1 and c == -1:
             break
        print("w(%d, %d, %d) = %d"%(a,b,c,w(a,b,c)))