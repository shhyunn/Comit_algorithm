import sys
import collections
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt")
input = sys.stdin.readline
def rounded(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    elif n - int(n) <= -0.5:
        return int(n) - 1
    else:
        return int(n)
    
N = int(input())
mid = (N+1)//2

#산술평균, 중앙값,최빈값,범위 (최빈값 여러개일 경우, 두번째로 작은 값)
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

print(rounded(sum(arr)/N))
print(arr[mid-1])

#최빈값
bins = collections.Counter(arr).most_common()
res = [k for k,v in bins if v == bins[0][1]]
if len(res) > 1:
    print(res[1])
else:
    print(res[0])

print(arr[-1]-arr[0])