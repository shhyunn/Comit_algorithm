import sys
from collections import deque
input = sys.stdin.readline
A,B,C =map(int, input().split())

'''
지수법칙 : A^(M+N) = A^M+A^N
나머지분배법칙 : (A*B)%C = (A%C)*(B%C)%C
'''
def multi(a,n):#a를 n번 곱한 수
    if n == 1: #1이라면 바로 나머지 반환
        return a%C
    else: #n이 2 이상이라면
        temp = multi(a,n//2)#절반의 값 구하기
        if n%2 == 0: #n이 짝수라면
            return (temp*temp)%C #그 나머지를 곱하여 c로 나누기
        else:
            return (temp*temp*a)%C #홀수이니 a도 곱해주기

print(multi(A,B))