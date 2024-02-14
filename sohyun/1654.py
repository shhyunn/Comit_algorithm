import sys
#n개의 랜선 만들기
#k개의 랜선을 n개의 같은 길이의 랜선으로 만들기
#만들 수 있는 최대 랜선의 길이?
def binary(lst, start, end, n, prev): #start: 가장 짧은 길이 & #end: 가장 긴 길이
    if start > end:
        return prev
    
    mid = ( start + end ) // 2
    sum = 0

    for ls in lst:
        sum += (ls // mid) #가장 짧은 길이와 가장 긴 길이의 평균으로 나눈다

    if n <= sum:
        return binary(lst, mid+1, end, n, max(prev,mid)) #랜선 개수 동일 시 max값으로 return
    
    elif n > sum:
        return binary(lst, start, mid-1, n, prev)
    
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")   
input = sys.stdin.readline
K,N = map(int,input().split())
lst = []
for _ in range(K):
    lst.append(int(input()))
    #802,743,457,539

print(binary(lst, 1, max(lst), N, -1))