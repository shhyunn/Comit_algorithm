
#키의 길이대로 나열, 열단위로 정렬, 키의 문자를 기준으로 정렬
#키와 암호문 -> 평문을 구하라

import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
keys = input()
code = input()
col = len(code)//len(keys)

store = [[] for _ in range(len(keys))]
id = [i for i in range(len(keys))]
sorted_id = sorted(id, key=lambda x: keys[x])

index = 0
for i in range(0,len(code)-col+1,col):
    for j in range(i,i+col):
        store[index].append(code[j])
    index += 1

lst2 = sorted(store,key=lambda x:sorted_id[store.index(x)]) #store를 정렬하라
k=0
res = ""
while k < col:
    for j in range(len(keys)):
        res += lst2[j][k]
    k+=1
print(res)

'''
import sys
sys.stdin = open("C:\\Users\\LG\\proj\\comit\\sohyun\\input.txt","r")
input = sys.stdin.readline

key = list(input().strip())
code = input().strip()
mul = len(code) // len(key)

deKey = sorted(key) #정렬키
kIdx = []
for k in key:
    idx = deKey.index(k)
    kIdx.append(idx)
    deKey[idx] = ""
decode = []
for cnt in range(len(code)): #암호길이
    r = kIdx[cnt % len(kIdx)] #키 인덱스
    c = cnt // len(kIdx)

    ch = code[r * mul + c]#
    decode.append(ch) 

print("".join(decode))'''

