import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
arr_sum = set()
for x in arr:
    for y in arr:
        arr_sum.add(x+y)

def check():
    global answer
    for i in range(N-1,-1,-1):
        for j in range(i+1):
            if arr[i] - arr[j] in arr_sum:
                answer = arr[i]
                return

answer = 0
check()
print(answer)
#x+y+z = k일 때, k-x = y+z 일단 모든 합 구하기, 가장 큰 값에서 가장 작은 값을 뺀 값부터 차례대로 탐색