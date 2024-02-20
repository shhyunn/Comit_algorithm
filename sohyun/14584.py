import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

strr = input().strip()
to_num = [ord(ch) for ch in strr]
alpha = [chr(num) for num in range(ord("a"),ord("z")+1)]

N = int(input())
dic = []
for _ in range(N):
    dic.append(input().strip())

def find_alpha(alpha, to_num, dic):
    ll = len(alpha)
    for i in range(ll+1):
        apply = [alpha[(n+i)%ll] for n in to_num]
        apply_strr = "".join(apply)
        for word in dic:
            if word in apply_strr:
                return apply_strr

print(find_alpha(alpha, to_num , dic))