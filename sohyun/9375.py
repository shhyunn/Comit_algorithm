import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

#한번 입은 조합 사용 안함
N = int(input())

for _ in range(N):
    t = int(input())
    dic = {}
    for _ in range(t):
        #의상의 이름과 의상의 종류
        a,b = input().rstrip().split()
        if b in dic.keys():
            dic[b] += 1
        else:
            dic[b] = 1
    
    sum = 1
    for i in dic.keys():
        sum *= (dic[i]+1)
    
    sum -= 1 #공집합 빼기
    print(sum)
