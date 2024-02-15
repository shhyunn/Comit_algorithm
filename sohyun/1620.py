import sys
sys.stdin = open("C:\\Users\\LG\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline
N,M = map(int, input().split()) #n 포켓몬 개수, m 문제의 개수
dic = {}
dic2 = {}

for i in range(N):
    strr = input().rstrip()
    dic[i+1] = strr
    dic2[strr] = i+1

for _ in range(M):
    #알파벳 - 포켓몬 번호
    #숫자 - 번호에 해당하는 문자 입력
    question = input().rstrip()
    if question.isdigit():
        print(dic[int(question)])
    else:
        print(dic2[question])