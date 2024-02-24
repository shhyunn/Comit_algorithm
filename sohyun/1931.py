import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N = int(input())

lst = []
for _ in range(N):
    start, end = map(int, input().split())
    lst.append([start,end])

lst.sort()
arr = []
start = 0
for a,b in lst:
    if arr == []:
        arr.append(b)
        start = a

    elif a >= arr[-1]:
        arr.append(b)
        start = a
    else: #시작 시간이 끝나는 시간과 겹쳐질경우, 이전 시작시간과 끝나는 시간 사이
        if b <= arr[-1]: #현재 끝나는 시간보다 빨리 끝날 경우
            arr.pop()
            arr.append(b)
            start = a

print(len(arr))
