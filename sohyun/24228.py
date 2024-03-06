import sys
input = sys.stdin.readline

#n종류의 젓가락이 충분히 많이 들어있음!!!!1
N,R = map(int, input().split())
print((N-1)+R*2)
